#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''
import sys

lRDpath = "//kaixuan.com/kx/Resouce/Support/KX/maya2014/modules/lightRender/scripts"

if lRDpath not in sys.path:
    sys.path.append(lRDpath)
    
    
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./plugins')
nuke.pluginAddPath('./icons')