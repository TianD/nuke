#coding:utf-8
'''
Created on 2016年5月30日 下午3:37:57

@author: TianD

@E_mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description: define delegate

'''

from PyQt4 import QtCore, QtGui
from _functools import partial

class ProgressBarDelegate(QtGui.QStyledItemDelegate):
    
    def __init__(self, parent = None):
        super(ProgressBarDelegate, self).__init__(parent)
        self.parent = parent
        
    def paint(self, painter, option, index):
   
        value = index.data(QtCore.Qt.DisplayRole)
        value,_ = value.toInt()
           
        # fill style options with item data
        style = QtGui.QApplication.style()
        opt = QtGui.QStyleOptionProgressBarV2()
        opt.maximum = 100
        opt.progress = value
        opt.rect = option.rect
        opt.textVisible = True
        opt.text = str(value)
        opt.textAlignment = QtCore.Qt.AlignHCenter
        # draw item data as CheckBox
        style.drawControl(QtGui.QStyle.CE_ProgressBar, opt, painter)


class ComboBoxDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, options, parent = None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.parent = parent
        self.__items = options
        
    def createEditor(self, parent, option, index):
        editor = QtGui.QComboBox(parent)
        for i in range(len(self.__items)):
            editor.insertItem(i, self.__items[i].toString(), userData=QtCore.QVariant())
        return editor
    
    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole).toString()
        editor.setCurrentIndex(editor.findText(value))
        
    def setModelData(self, editor, model, index):
        value = editor.currentIndex()
        model.setData(index, editor.itemData(value, QtCore.Qt.DisplayRole | QtCore.Qt.EditRole))