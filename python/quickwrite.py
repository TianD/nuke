#coding:utf-8
'''
Created on 2015/7/15

@author: TianD
'''
import sys,os
import re
from string import zfill

lRDpath = "//kaixuan.com/kx/Resouce/Support/KX/maya2014/modules/lightRender/scripts"

if lRDpath not in sys.path:
    sys.path.append(lRDpath)
    
import nuke

import lightRenderData as lRD

def quickWrite():
    
    #read sceneName from nuke root Node
    root = nuke.toNode("root")
    sceneName = root.name().split("/")[-1].split(".")[0]
    
    nameMatch = lRD.ProjNameMatch()
    nameMatch.fileName = sceneName
    uploadPath = nameMatch.getUploadServerPath().replace("Images", "Comp")
    versionNumber = sceneName.split("_")[-1]
    format = ".%04d.tga"
    
    #判断路径是否存在, 判断路径是否是空
    if os.path.exists(uploadPath):
        subdirs = os.listdir(uploadPath)
        #判断有木有子文件夹, 即有木有版本号文件夹
        if subdirs:
            lastDir = subdirs[-1]
            #判断版本文件夹内是否有文件
            if os.listdir(uploadPath + "/" + lastDir):
                #如果非空, 则创建新的版本文件夹
                lastNum = int(re.findall("\d+", lastDir)[-1])
                prefix = re.findall("[a-zA-Z]", lastDir)[0]
                version = prefix + str(lastNum+1).zfill(3)
                fullPath = uploadPath + "/" + version
                newSceneName = sceneName.replace(versionNumber, version)
            else :
                #如果为空, 则输出到这个版本内
                fullPath = uploadPath + "/" + lastDir
                newSceneName = sceneName.replace(versionNumber, lastDir)
                
        else :
            fullPath = uploadPath + "/c001"
            newSceneName = sceneName.replace(versionNumber, "c001")
        try:
            os.makedirs(fullPath)
        except Exception,e:
            print e
    else :
        fullPath = uploadPath + "/c001"
        try:
            os.makedirs(fullPath)
        except Exception,e:
            print e
        newSceneName = sceneName.replace(versionNumber, "c001")    
    fullName = fullPath + "/" + newSceneName + format
    
    #does has selected
    selectedNodes = nuke.selectedNodes()
    if selectedNodes :
        #get node's position in node graph
        x = selectedNodes[-1].xpos() + 100
        y = selectedNodes[-1].ypos() + 100
        #create write node
        writeNode = nuke.nodes.Write(channels = "rgba", colorspace = "default(sRGB)", file = fullName, file_type = "targa", xpos = x, ypos = y, inputs = [selectedNodes[-1]])
    else :
        #if no selected node use the node graph center
        x, y = nuke.center()
        writeNode = nuke.nodes.Write(channels = "rgba", colorspace = "default(sRGB)", file = fullName, file_type = "targa", xpos = x, ypos = y)
    writeNode["compression"].setValue("none")
    return writeNode
