#coding:utf-8
'''
Created on 2016年6月6日 下午3:23:01

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: define functions

'''
import sys
 
a = "Z:\\Resouce\\Support\\KX\\maya2014\\modules\\TianD_KX_TOOL\\scripts"
b = "Z:\\Resouce\\Support\\KX\\maya2014\\modules\\lightRender\\scripts"
sys.path.append(a)
sys.path.append(b)

import os, os.path, shutil
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
                    result.append([0, os.path.join(root, v), '', option, 0])
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
            result.append([0, os.path.join(root, key), frameRange, option, 0])
            
    return result

def createPath(filePath, add):
    textName = os.path.basename(filePath)
    pnm = ProjNameMatch()
    pnm.setFileName(textName)
    pnm.setPrefix(mod=1)
    version = pnm.getResults('version_number')
    uploadPath = pnm.getUploadServerPath(mod='Images')
    if optionDic[u"%s" %add] :
        uploadPath = os.path.join(uploadPath, optionDic[u"%s" %add], version)
    else :
        uploadPath = os.path.join(uploadPath, version)
    
    uploadPath = uploadPath.replace("//kaixuan.com/kx/Proj/SENBA/Production/Render", "E:") 
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
    
    sourceFile = os.path.join(textPath, fileName)
    uploadFile = os.path.join(uploadPath, fileName)
    
    try:
        shutil.copy2(sourceFile, uploadFile)
    except:
        raise IOError, "failure"
    #print uploadFile
    return uploadFile
    
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
        
if __name__ == "__main__":
    '''
    [
    ['a','ROCK_001_001_001_an_c001', '1001-1100', QtCore.QVariant('Left'), 0],
    ['b','ROCK_002_002_002_an_c001', '1001-1110', QtCore.QVariant('Right'), 0],
    ['b','ROCK_003_003_003_an_c001', '1001-1110', QtCore.QVariant('Right'), 0]
    ]
    '''
    print parseCmd(['E:/rock_sq/sq001/sc001/stereoCameraLeft/c002\\SB_102_001_001_cp_c002.1001.tga', []], mod = 1)
    #print getFrames("1001-1010,1012-1014")
    #print getFrames("1001")
    #print getFrames("1001-1010,1012-1014,1016,1020-1022")
    #print copyCmd("E:\\senba_sq\\sq001\\sc001\\c001\\SB_102_001_001_cp_c001.1001.tga", "Normal")