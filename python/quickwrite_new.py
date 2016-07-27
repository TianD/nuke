#coding:utf-8
'''
Created on 2015/7/15

@author: TianD
'''
import sys,os
import re
from string import zfill

import nuke, nukescripts

import lightRenderData as lRD
import kxTool
from _functools import partial
                        
def quickWrite():
    #read sceneName from nuke root Node
    root = nuke.toNode("root")
    
    sceneName = root.name().split("/")[-1].split(".")[0]
    
    if sceneName == 'Root':
        raise ImportError, "请先打开正确命名的文件" 
    
    nameMatch = lRD.ProjNameMatch()
    nameMatch.setFileName(sceneName)
    nameMatch.setPrefix(mod=1)
    projName = nameMatch.getPorjName()
    
    uploadPath = nameMatch.getUploadServerPath().replace("Images", "Comp")
    
    kx = kxTool.KXTool()
    if kx.stereoDic.has_key(projName):
        if kx.stereoDic[projName] == 1:   
            file_l = createOutPath(sceneName, uploadPath, 'stereoCameraLeft')
            file_r = replaceOutPath(file_l)

            setNodeValue(file_r, file_l)
        
    else :
        file = createOutPath(sceneName, uploadPath)

        setNodeValue(file)
        
def setNodeValue(*files):
    
    # set view for stereo
    nukescripts.stereo.setViewsForStereo()
    
    #does has selected
    selectedNodes = nuke.selectedNodes()
    if selectedNodes :
        #get node's position in node graph
        x = selectedNodes[-1].xpos() + 100
        y = selectedNodes[-1].ypos() + 100
        #create write node
        writeNode = nuke.nodes.Write(channels = "rgba", colorspace = "default(sRGB)", file = files[0], file_type = "targa", xpos = x, ypos = y, inputs = [selectedNodes[-1]])
    else :
        #if no selected node use the node graph center
        x, y = nuke.center()
        writeNode = nuke.nodes.Write(channels = "rgba", colorspace = "default(sRGB)", file = files[0], file_type = "targa", xpos = x, ypos = y)
    writeNode["compression"].setValue("none")
    if len(files) == 2:
        writeNode['file'].splitView('right')
        writeNode['file'].setValue(files[1])
    return writeNode

def createOutPath(sceneName, uploadPath, add= None):
       
    if add:
        uploadPath = uploadPath + "/" + add
    versionNumber = sceneName.split("_")[-1]
    format = ".%04d.tga"
    
    #判断路径是否存在, 判断路径是否是空
    if os.path.exists(uploadPath):
        subdirs = [d for d in os.listdir(uploadPath) if os.path.isdir(d)]
        #判断有木有子文件夹, 即有木有版本号文件夹
        if subdirs:
            lastDir = subdirs[-1]
            #判断版本文件夹内是否有文件
            if os.listdir(uploadPath + lastDir):
                #如果非空, 则创建新的版本文件夹
                lastNum = int(re.findall("\d+", lastDir)[-1])
                prefix = re.findall("[a-zA-Z]", lastDir)[0]
                version = prefix + str(lastNum+1).zfill(3)
                fullPath = uploadPath + version
                newSceneName = sceneName.replace(versionNumber, version)
            else :
                #如果为空, 则输出到这个版本内
                fullPath = uploadPath + lastDir
                newSceneName = sceneName.replace(versionNumber, lastDir)
                
        else :
            fullPath = uploadPath + "/c001"
            newSceneName = sceneName.replace(versionNumber, "c001")
        try:
            os.makedirs(fullPath)
        except Exception,e:
            print e
    else  :
        fullPath = uploadPath + "/c001"
        try:
            os.makedirs(fullPath)
        except Exception,e:
            print e
        newSceneName = sceneName.replace(versionNumber, "c001")    
    fullName = fullPath + "/" + newSceneName + format
    
    return fullName

def replaceOutPath(sourcePath, froms = 'stereoCameraLeft', tos = 'stereoCameraRight'):
    newPath = sourcePath.replace(froms, tos)
    dir = os.path.dirname(newPath)
    file = os.path.basename(newPath)
    if os.path.exists(dir):
        return newPath
    else :
        try:
            os.makedirs(dir)
        except Exception, e:
            print e
            return
        return newPath
    