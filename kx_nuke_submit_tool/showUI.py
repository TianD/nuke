#coding:utf-8
'''
Created on 2016年5月30日 下午12:00:30

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: define ui 

'''
import sys
import os.path
from PyQt4 import QtCore, QtGui
import nuke
from _functools import partial

from kx_nuke_submit_tool import Ui_SubmissionWidget
from kx_nuke_submit_tool_delegate import ProgressBarDelegate, ComboBoxDelegate
from kx_nuke_submit_tool_model import TableModel
from kx_nuke_submit_tool_thread import SubmitWorker, LoadWorker

class SubmissionWindow(QtGui.QWidget, Ui_SubmissionWidget):
    
    def __init__(self, parent = None):
        super(SubmissionWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.submitPushButton.clicked.connect(self.submitCmd)

        self.initTableView()
        self.loadCmd()
                
    def initTableView(self):
        headerLabels = [u'状态', u'名称', u'帧数', u'选项', u'进度']
        options = [QtCore.QVariant('Normal'), QtCore.QVariant('Left'), QtCore.QVariant('Right')]
        tabledata = []
        self.contentModel = TableModel(headerLabels, tabledata)
        self.tableView.setModel(self.contentModel)
        pbd = ProgressBarDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(4, pbd)
        cbd = ComboBoxDelegate(options, self.tableView)
        self.tableView.setItemDelegateForColumn(3, cbd)
    
    def setTableData(self, data):
        print data
        rowCount = self.contentModel.rowCount()
        self.contentModel.insertRows(rowCount, data)
#                 
    def submitCmd(self):
        '''
        submit images from sw. to production path
        '''
        model = self.tableView.model()
        row = model.rowCount()
        column = model.columnCount() 
        indexLst = [model.index(i,4) for i in range(row)]
        threads = [SubmitWorker() for i in range(row)]
        for i in range(row):
            index = indexLst[i]
            subThread = threads[i]
            subThread.progressSignal.connect(partial(model.setData, index))
            subThread.start(model.getData()[i])
            subThread.finishSignal.connect(partial(self.setFlagCmd, index))
    
    def setFlagCmd(self, index, int):
        model = index.model()
        row = index.row()
        column = 0
        flagIndex = model.index(row, 0)
        if int == 100:
            model.setData(flagIndex, 2)
        else :
            model.setData(flagIndex, 1)
            
    def loadCmd(self):
        paths = []
        for node in nuke.allNodes("Read"):
            file = os.path.basename(node["file"].getValue())
            dir = os.path.dirname(node["file"].getValue())
            first = node['first'].value()
            last = node['last'].value()
            if first == last:
                frameRange = []
            else :
                frameRange = range(node['first'].value(), node['last'].value()+1)
            paths.append([os.path.join(dir, file),frameRange])
        self.loadThread = LoadWorker()
        self.loadThread.start(paths)
        self.loadThread.fileSignal.connect(self.setTableData)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui=SubmissionWindow()
    ui.show()
    app.exec_()
    