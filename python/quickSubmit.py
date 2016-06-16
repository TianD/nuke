#coding:utf-8
'''
Created on 2016年6月16日 下午4:24:48

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: call kx_nuke_submit_tool

'''
from nukescripts import panels
from kx_nuke_submit_tool import showUI
from PyQt4 import QtGui
reload(showUI)

def quickSubmit():
    for widget in QtGui.QApplication.allWidgets():
        name = widget.objectName()
        if 'SubmissionWindow' in name:
            widget.deleteLater()
    
    pane = nuke.getPaneFor('Properties.1')
    panels.registerWidgetAsPanel('showUI.SubmissionWindow', '腾清素材上传_NUKE', 'uk.co.thefoundry.SubmissionWindow', True).addToPane(pane)