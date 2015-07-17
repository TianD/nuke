#coding:utf-8
'''
Created on 2015/7/17

@author: TianD
'''
import os
import nuke
import copyTree
    
import lightRenderData as lRD

def replaceFootages():
    
    footages = dict()
    for node in nuke.allNodes("Read"):
        file = os.path.basename(node["file"].getValue())
        dir = os.path.dirname(node["file"].getValue())
        footages.setdefault(node.fullName(), [file,dir])
        

    for key, value in footages.items():

        filename = value[0]
        d = value[1]
        
        #first, upload footages to server
        nameMatch = lRD.ProjNameMatch()
        nameMatch.fileName = filename
        
        uploadPath = nameMatch.getUploadServerPath()
        
        newd = uploadPath + "/" + d.split("/")[-1]
        
        if os.path.exists(newd):
            if os.listdir(newd):
                if nuke.ask('!!!素材已经存在, 是否覆盖!!!'):
                    pass
                else :
                    read = nuke.toNode(key)
                    newValue = read["file"].getValue().replace(d, newd)
                    read["file"].setValue(newValue)
                    continue
        else :
            os.makedirs(newd)
        copyTree.copytree(d, newd)
        
        read = nuke.toNode(key)
        newValue = read["file"].getValue().replace(d, newd)
        read["file"].setValue(newValue)
        
    
