# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Scripts\Eclipse\nuke\kx_submission_tool\source\kx_nuke_submit_tool.ui'
#
# Created: Mon Jun 13 15:35:49 2016
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
        SubmissionWidget.resize(623, 354)
        self.verticalLayout = QtGui.QVBoxLayout(SubmissionWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(SubmissionWidget)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.submitPushButton = QtGui.QPushButton(SubmissionWidget)
        self.submitPushButton.setMaximumSize(QtCore.QSize(6000, 6000))
        self.submitPushButton.setObjectName(_fromUtf8("submitPushButton"))
        self.verticalLayout.addWidget(self.submitPushButton)

        self.retranslateUi(SubmissionWidget)
        QtCore.QMetaObject.connectSlotsByName(SubmissionWidget)

    def retranslateUi(self, SubmissionWidget):
        SubmissionWidget.setWindowTitle(_translate("SubmissionWidget", "kx_nuke_submit_tool", None))
        self.submitPushButton.setToolTip(_translate("SubmissionWidget", "开始上传", None))
        self.submitPushButton.setText(_translate("SubmissionWidget", "上传", None))

