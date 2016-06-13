#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''
import sys

lRDpath = "//kaixuan.com/kx/Resouce/Support/KX/maya2014/modules/lightRender/scripts"
projectDicPath = 'Z:/Resouce/Support/KX/maya2014/modules/TianD_KX_TOOL/scripts'

kxPath = [lRDpath, projectDicPath]

for path in kxPath:
    if path not in sys.path:
        sys.path.append(path)
    
    
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./plugins')
nuke.pluginAddPath('./icons')