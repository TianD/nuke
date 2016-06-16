# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Scripts\Eclipse\nuke\kx_nuke_submit_tool\source\kx_nuke_submit_tool.ui'
#
# Created: Thu Jun 16 15:37:52 2016
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SubmissionWidget(object):
    def setupUi(self, SubmissionWidget):
        SubmissionWidget.setObjectName(_fromUtf8("SubmissionWidget"))
        SubmissionWidget.resize(623, 375)
        SubmissionWidget.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"    border:none;\n"
"}\n"
"QPushButton#submitPushButton \n"
"{\n"
"    image: url(:/submitIcon/submit.png);\n"
"}\n"
"QPushButton#submitPushButton:hover \n"
"{\n"
"    image: url(:/submitIcon/submit_color.png);\n"
"}\n"
"QPushButton#removePushButton \n"
"{\n"
"    image: url(:/removeIcon/remove.png);\n"
"}\n"
"QPushButton#removePushButton:hover \n"
"{\n"
"    image: url(:/removeIcon/remove_color.png);\n"
"}\n"
"QPushButton#resetPushButton \n"
"{\n"
"    image: url(:/resetIcon/reset.png);\n"
"}\n"
"QPushButton#resetPushButton:hover \n"
"{\n"
"    image: url(:/resetIcon/reset_color.png);\n"
"}\n"
"QPushButton#lrPushButton \n"
"{\n"
"    image: url(:/lightIcon/light.png);\n"
"}\n"
"QPushButton#lrPushButton:hover \n"
"{\n"
"    image: url(:/lightIcon/light_color.png);\n"
"}\n"
"QPushButton#fxPushButton \n"
"{\n"
"    image: url(:/effectIcon/effect.png);\n"
"}\n"
"QPushButton#fxPushButton:hover \n"
"{\n"
"    image: url(:/effectIcon/effect_color.png);\n"
"}"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(SubmissionWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableView = QtGui.QTableView(SubmissionWidget)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setToolTip(_fromUtf8(""))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_3.addWidget(self.tableView)
        self.btnHBoxLayout = QtGui.QHBoxLayout()
        self.btnHBoxLayout.setObjectName(_fromUtf8("btnHBoxLayout"))
        self.departmentVBoxLayout = QtGui.QVBoxLayout()
        self.departmentVBoxLayout.setObjectName(_fromUtf8("departmentVBoxLayout"))
        self.fxPushButton = QtGui.QPushButton(SubmissionWidget)
        self.fxPushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.fxPushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.fxPushButton.setText(_fromUtf8(""))
        self.fxPushButton.setIconSize(QtCore.QSize(50, 50))
        self.fxPushButton.setObjectName(_fromUtf8("fxPushButton"))
        self.departmentVBoxLayout.addWidget(self.fxPushButton)
        self.lrPushButton = QtGui.QPushButton(SubmissionWidget)
        self.lrPushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.lrPushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.lrPushButton.setText(_fromUtf8(""))
        self.lrPushButton.setIconSize(QtCore.QSize(50, 50))
        self.lrPushButton.setObjectName(_fromUtf8("lrPushButton"))
        self.departmentVBoxLayout.addWidget(self.lrPushButton)
        self.btnHBoxLayout.addLayout(self.departmentVBoxLayout)
        self.setVBoxLayout = QtGui.QVBoxLayout()
        self.setVBoxLayout.setSpacing(6)
        self.setVBoxLayout.setObjectName(_fromUtf8("setVBoxLayout"))
        self.resetPushButton = QtGui.QPushButton(SubmissionWidget)
        self.resetPushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.resetPushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.resetPushButton.setStyleSheet(_fromUtf8("border:none;"))
        self.resetPushButton.setText(_fromUtf8(""))
        self.resetPushButton.setIconSize(QtCore.QSize(50, 50))
        self.resetPushButton.setObjectName(_fromUtf8("resetPushButton"))
        self.setVBoxLayout.addWidget(self.resetPushButton)
        self.removePushButton = QtGui.QPushButton(SubmissionWidget)
        self.removePushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.removePushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.removePushButton.setStyleSheet(_fromUtf8("border:none;"))
        self.removePushButton.setText(_fromUtf8(""))
        self.removePushButton.setIconSize(QtCore.QSize(50, 50))
        self.removePushButton.setObjectName(_fromUtf8("removePushButton"))
        self.setVBoxLayout.addWidget(self.removePushButton)
        self.btnHBoxLayout.addLayout(self.setVBoxLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btnHBoxLayout.addItem(spacerItem)
        self.submitPushButton = QtGui.QPushButton(SubmissionWidget)
        self.submitPushButton.setMinimumSize(QtCore.QSize(200, 100))
        self.submitPushButton.setMaximumSize(QtCore.QSize(6000, 6000))
        self.submitPushButton.setText(_fromUtf8(""))
        self.submitPushButton.setIconSize(QtCore.QSize(100, 100))
        self.submitPushButton.setObjectName(_fromUtf8("submitPushButton"))
        self.btnHBoxLayout.addWidget(self.submitPushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btnHBoxLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.btnHBoxLayout)

        self.retranslateUi(SubmissionWidget)
        QtCore.QMetaObject.connectSlotsByName(SubmissionWidget)

    def retranslateUi(self, SubmissionWidget):
        SubmissionWidget.setWindowTitle(_translate("SubmissionWidget", "kx_nuke_submit_tool", None))
        self.fxPushButton.setToolTip(_translate("SubmissionWidget", "仅列出特效部门的素材", None))
        self.lrPushButton.setToolTip(_translate("SubmissionWidget", "仅列出灯光部门的素材", None))
        self.resetPushButton.setToolTip(_translate("SubmissionWidget", "刷新重置面板", None))
        self.removePushButton.setToolTip(_translate("SubmissionWidget", "移除所选择的Item", None))
        self.submitPushButton.setToolTip(_translate("SubmissionWidget", "开始上传", None))

import kx_nuke_submit_tool_rc
