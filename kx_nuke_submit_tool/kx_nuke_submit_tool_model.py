#coding:utf-8
'''
Created on 2016年5月30日 下午12:04:18

@author: TianD

@E_mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: define model

'''

from PyQt4 import QtCore, QtGui

class TableModel(QtCore.QAbstractTableModel):
    
    def __init__(self, header, data, parent = None):
        super(TableModel, self).__init__(parent)
        self.__header = header
        self.__data = data
    
    def getData(self):
        return self.__data
    
    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.__data)
    
    def columnCount(self, parent = QtCore.QModelIndex()):
        return len(self.__header)
        
    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                return self.__header[section]
            else :
                return section+1
            
    def data(self, index, role = QtCore.Qt.DisplayRole):
        
        if not self.rowCount():
            return 
        
        row = index.row()
        column = index.column()
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if column != 0:
                value = self.__data[row][column]
                return value
        
        if role == QtCore.Qt.DecorationRole :
            if column == 0:
                value = self.__data[row][column]
                if value == 2:
                    return QtGui.QColor(0,255,0)
                elif value == 1:
                    return QtGui.QColor(255,0,0)
                else :
                    return 
            
    def flags(self, index):
        column = index.column()
        if column == 4 :
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
    
    def setData(self, index, value, role = QtCore.Qt.DisplayRole):
                
        if role == QtCore.Qt.EditRole or role == QtCore.Qt.DisplayRole or role == QtCore.Qt.DecorationRole:
            row = index.row()
            column = index.column()
            
            value = value
            if column == 5 or column == 0 :
                self.__data[row][column] = value
                self.dataChanged.emit(index, index)
                return True               
            else :
                if value.isValid():
                    self.__data[row][column] = value
                    self.dataChanged.emit(index, index)
                return True
        
        return False   
    
    def insertRows(self, row, data, parent = QtCore.QModelIndex()):
        count = len(data)
        self.beginInsertRows(parent, row, row + count -1)
        for i in range(count-1,-1,-1):
            self.__data.insert(row, data[i])
        self.endInsertRows()
        return
    
    def removeRow(self, row, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        del self.__data[row]
        self.endRemoveRows()