#coding:utf-8
'''
Created on 2016年6月6日 下午3:23:01

@author: TianD

@E_mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: define functions

'''
# import sys
#  
# a = "Z:\\Resouce\\Support\\KX\\maya2014\\modules\\TianD_KX_TOOL\\scripts"
# b = "Z:\\Resouce\\Support\\KX\\maya2014\\modules\\lightRender\\scripts"
# sys.path.append(a)
# sys.path.append(b)

import os, os.path, shutil
import nuke
from PyQt4 import QtCore
from sequenceFileDetection import SequenceFileDetection
from lightRenderData import ProjNameMatch


optionDic = {
             'Left':'stereoCameraLeft',
             'Right':'stereoCameraRight',
             'Normal':None
             }

def parseCmd(filePath, mod = 1):
    root = os.path.dirname(filePath[0])
    file = os.path.basename(filePath[0]).split(".")[0]
    ext = os.path.basename(filePath[0]).split(".")[-1]
    frameRange = filePath[1]
    nodeName = filePath[-1]
    if frameRange:
        files = ["{0}.{1}.{2}".format(file, i, ext) for i in frameRange]
    else :
        tempFrame = os.path.basename(filePath[0]).split(".")[1]
        files = ["{0}.{1}.{2}".format(file, tempFrame, ext)]
    result = []
    option = QtCore.QVariant("Normal")
    """将序列文件转换成项目需要的ffmpeg格式"""
    sfd = SequenceFileDetection()
    sfd.setSequenceFiles(files)
    dic = sfd.getSequenceInfo(mod)
    if 'stereoCameraLeft' in root or 'CamL' in root:
        option = QtCore.QVariant("Left")
    elif 'stereoCameraRight' in root or 'CamR' in root:
        option = QtCore.QVariant("Right")
    else :
        option = QtCore.QVariant("Normal")
    for key, value in dic.iteritems():
        if key == "separateFiles":
            pnm = ProjNameMatch()
            for v in value:
                pnm.setFileName(v)
                if pnm.matchProjName():
                    result.append([0, nodeName, os.path.join(root, v), '', option, 0])
        else :
            framePrefix = key.split('.')[-2].split('%')[0]
            frameStart = value[0]
            frameEnd = value[1]
            frameMiss = value[-1]
            if frameMiss :
                miss = '-'.join([','.join(['{0}'.format(f-1), '{0}'.format(f+1)]) for f in frameMiss])
                frameRange = "{0}{1}-{3}-{0}{2}".format(framePrefix, frameStart, frameEnd, miss)
            else :
                frameRange = "{0}{1}-{0}{2}".format(framePrefix, frameStart, frameEnd)
            result.append([0, nodeName, os.path.join(root, key), frameRange, option, 0])
            
    return result

def createPath(filePath, add):
    textName = os.path.basename(filePath)
    pnm = ProjNameMatch()
    pnm.setFileName(textName)
    pnm.setPrefix(mod=1)
    version = pnm.getResults('version_number')
    describ = os.path.basename(os.path.dirname(filePath))
    elems = [optionDic[u"%s" %add], version]
    if describ != version :
        elems.append(describ)
    uploadPath = pnm.getUploadServerPath(mod='Images')
    for elem in elems:
        if elem:
            uploadPath = os.path.normpath(os.path.join(uploadPath, elem))
        else :
            pass
    
#     normalserverPath = os.path.normpath("//kaixuan.com/kx/Proj")
#     serverPath = "//kaixuan.com/kx/Proj"
#     uploadPath = uploadPath.replace(serverPath, "E:").replace(normalserverPath, "E:")
    
    if os.path.exists(uploadPath):
        #print "{0} has existed".format(uploadPath)
        pass
    else :
        try:
            os.makedirs(uploadPath)
        except:
            raise OSError, "check property"
        
    return uploadPath

def copyCmd(filePath, uploadPath, frame = None):
    textName = os.path.basename(filePath)
    textPath = os.path.dirname(filePath)
       
    if frame :
        fileName = "{0}.{1}.{2}".format(textName.split(".")[0], frame, textName.split(".")[-1])
    else :
        fileName = "{0}".format(textName)
    
    sourceFile = os.path.normpath(os.path.join(textPath, fileName))
    uploadFile = os.path.normpath(os.path.join(uploadPath, fileName))

    if sourceFile.replace("z:", os.path.normpath("//kaixuan.com/kx")).replace("Z:", os.path.normpath("//kaixuan.com/kx")) == uploadFile:
        return uploadFile
    
#     if sourceFile == uploadFile:
#         return uploadFile
           
    try:
        shutil.copy2(sourceFile, uploadFile)
    except:
        raise IOError, "failure"
    #print uploadFile
    return uploadFile

def setNodeFileValue(nodeName, uploadPath):
    node = nuke.toNode(nodeName)
    value = node['file'].getValue()
    path = os.path.dirname(value)
    newValue = os.path.normpath(value.replace(path, uploadPath)).replace("\\","/")
    node['file'].setValue(newValue)
    return nodeName
    
def getFrames(frameRange):
    sections = frameRange.split(",")
    frameLst = []
    for section in sections:
        startEnd = section.split("-")
        if len(startEnd) == 1:
            start = startEnd[0]
            end = startEnd[0]
        else :
            start, end = startEnd
        thisRange = range(int(start), int(end)+1)
        frameLst.extend(thisRange)
    return frameLst
        
def getDepartmentInfo(fileName):
    pnm = ProjNameMatch()
    pnm.setFileName(fileName)
    pnm.setPrefix(mod=1)
    department = pnm.getResults('process_name')
    return department

if __name__ == "__main__":
    '''
    [
    ['a','ROCK_001_001_001_an_c001', '1001-1100', QtCore.QVariant('Left'), 0],
    ['b','ROCK_002_002_002_an_c001', '1001-1110', QtCore.QVariant('Right'), 0],
    ['b','ROCK_003_003_003_an_c001', '1001-1110', QtCore.QVariant('Right'), 0]
    ]
    '''
    #print parseCmd(['E:/rock_sq/sq001/sc001/stereoCameraLeft/A_Clr\\ROCK_001_001_001_ef_AA1_c001.1001.exr', []], mod = 1)
    print createPath('Z:/Proj/ROCK/Production/Render/Images/ODD/ep001/sq011/sc084/stereoCameraLeft/c001/effect/ROCK_001_011_084_bigEffectLight_ef_c001/ROCK_001_011_084_bigEffectLight_ef_c001.%04d.tif', "Normal")
    #print getFrames("1001-1010,1012-1014")
    #print getFrames("1001")
    #print getFrames("1001-1010,1012-1014,1016,1020-1022")
    #print copyCmd("z:\\Proj\\ROCK\\Production\\Render\\Images\\ODD\\ep001\\sq001\\sc001\\stereoCameraLeft\\AA1\\c001\\ROCK_001_001_001_AA1_ef_c001.1001.exr", "//kaixuan.com/kx/Proj\\ROCK\\Production\\Render\\Images\\ODD\\ep001\\sq001\\sc001\\stereoCameraLeft\\AA1\\c001")