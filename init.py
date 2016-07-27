#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''
import sys

server_pyqt = "Z:/Resouce/Support/KX/maya2014/modules-external/PyQt4/scripts"
nuke.pluginAddPath(server_pyqt)


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