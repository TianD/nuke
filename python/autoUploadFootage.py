#coding:utf-8
'''
Created on 2015/7/17

@author: TianD
'''
import os
import nuke
import copyTree
    
import lightRenderData as lRD

def uploadFootages():

    #according to the user departments determine upload what type of footage in nuke
    #effects upload "_ef_"
    #render upload "_lr_"
    #other cannot upload any footage
    department = os.environ['KX_PROF'] 
        
    footages = dict()
    for node in nuke.allNodes("Read"):
        file = os.path.basename(node["file"].getValue())
        dir = os.path.dirname(node["file"].getValue())
        footages.setdefault(node.fullName(), [file,dir])
        

    for key, value in footages.items():
        
        filename = value[0]
        
        d = value[1]
        
        if "Z:" not in d:
            
            if department == 'effects':
                if "_ef_" in filename :
                    pass
                else :
                    continue
            
            elif department == 'render':
                if "_lr_" in filename :
                    pass
                else :
                    continue
            else :
                continue
            
            #first, upload footages to server
            nameMatch = lRD.ProjNameMatch()
            nameMatch.setFileName(filename)
            nameMatch.setPrefix(mod=1)
            
            uploadPath = nameMatch.getUploadServerPath()
            
            newd = uploadPath + d.split("/")[-1]
            
            if os.path.exists(newd):
                if os.listdir(newd):
                    if nuke.ask('!!!%s的素材已经存在, 是否覆盖!!!' %key):
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
            
        else :
            read = nuke.toNode(key)
            newValue = read["file"].getValue().replace("Z:", "//kaixuan.com/kx")
            read["file"].setValue(newValue)            
    
    nuke.message('更新完成')