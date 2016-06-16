#coding:utf-8
'''
Created on 2016年5月30日 下午12:00:30

@author: TianD

@E_mail: tiandao_dunjian@sina.cn

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
import kx_nuke_submit_tool_fun as fun


class SubmissionWindow(QtGui.QWidget, Ui_SubmissionWidget):
    
    def __init__(self, parent = None):
        super(SubmissionWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.submitPushButton.clicked.connect(self.submitCmd)
        self.resetPushButton.clicked.connect(self.resetCmd)
        self.removePushButton.clicked.connect(self.removeCmd)
        self.lrPushButton.clicked.connect(partial(self.departmentListCmd, ['lr', 'cp']))
        self.fxPushButton.clicked.connect(partial(self.departmentListCmd, ['ef']))
        
        self.resetCmd()
        
    def popup(self, pos):
        headerView = self.tableView.horizontalHeader()
        column = headerView.logicalIndexAt(pos)
        if column == 4:
            menu = QtGui.QMenu()
            leftAction = menu.addAction("Left")
            rightAction = menu.addAction("Right")
            normalAction = menu.addAction("Normal")
            action = menu.exec_(self.mapToGlobal(pos))
            if action == leftAction:
                self.setOptions(QtCore.QVariant('Left'))
            elif action == rightAction:
                self.setOptions(QtCore.QVariant('Right'))
            elif action == normalAction:
                self.setOptions(QtCore.QVariant('Normal'))
            else:
                pass
            
    
    def setOptions(self, value):
        model = self.tableView.model()
        rowCount = model.rowCount()
        for row in range(rowCount):
            index= model.index(row, 4)
            model.setData(index, value)
    
    def departmentListCmd(self, department):

        model = self.tableView.model()
        data = model.getData()
        newdata = []
        for subdata in data:
            filename = os.path.basename(subdata[2])
            process = fun.getDepartmentInfo(filename)
            if process in department:
                newdata.append(subdata)
        
        newmodel = TableModel(self.headerLabels, newdata)
        
        self.tableView.setModel(newmodel)
               
    def removeCmd(self):
        model = self.tableView.model()
        selected = self.tableView.selectedIndexes()
        rows = list(set([sel.row() for sel in selected]))
        rows.sort(reverse=True)
        for row in rows:
            model.removeRow(row)
        
    def resetCmd(self):
        self.initTableView()
        self.loadCmd()
                
    def initTableView(self):
        self.headerLabels = [u'状态', u'节点', u'名称', u'帧数', u'选项', u'进度']
        self.options = [QtCore.QVariant('Normal'), QtCore.QVariant('Left'), QtCore.QVariant('Right')]
        tabledata = []
        contentModel = TableModel(self.headerLabels, tabledata)
        self.tableView.setModel(contentModel)
        
        pbd = ProgressBarDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(5, pbd)
        cbd = ComboBoxDelegate(self.options, self.tableView)
        self.tableView.setItemDelegateForColumn(4, cbd)
        
        headerView = self.tableView.horizontalHeader()
        headerView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        headerView.customContextMenuRequested.connect(self.popup)
    
    def addTableData(self, data):
        model = self.tableView.model()
        rowCount = model.rowCount()
        model.insertRows(rowCount, data)
              
    def submitCmd(self):
        '''
        submit images from sw. to production path
        '''
        model = self.tableView.model()
        row = model.rowCount()
        column = model.columnCount() 
        indexLst = [model.index(i,5) for i in range(row)]
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
            paths.append([os.path.join(dir, file), frameRange, node.name()])
        self.loadThread = LoadWorker()
        self.loadThread.start(paths)
        self.loadThread.fileSignal.connect(self.addTableData)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui=SubmissionWindow()
    ui.show()
    app.exec_()
    