#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''

import quickwrite
import autoReplaceFootage

toolbar = nuke.menu("Nodes")
tdMenu = toolbar.addMenu("TianD", "TianD.png")

tdMenu.addCommand("Quick Write", "quickwrite.quickWrite()","alt+w","quickwrite.png")

tdMenu.addCommand("Auto Upload Footages", "autoUploadFootage.uploadFootages()","alt+r","uploadFootages.png")
