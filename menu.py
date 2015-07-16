#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''

import quickwrite

toolbar = nuke.menu("Nodes")
tdMenu = toolbar.addMenu("TianD", "TianD.png")

tdMenu.addCommand("Quick Write", "quickwrite.quickWrite()","alt+w","quickwrite.png")

