# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sheet.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 500)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 431, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.name = QtWidgets.QTextBrowser(self.groupBox_2)
        self.name.setGeometry(QtCore.QRect(10, 15, 181, 23))
        self.name.setObjectName("name")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 181, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 176, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hp = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.hp.setMaximumSize(QtCore.QSize(30, 30))
        self.hp.setObjectName("hp")
        self.horizontalLayout_2.addWidget(self.hp)
        self.ac = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.ac.setMaximumSize(QtCore.QSize(30, 30))
        self.ac.setObjectName("ac")
        self.horizontalLayout_2.addWidget(self.ac)
        self.speed = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.speed.setMaximumSize(QtCore.QSize(30, 30))
        self.speed.setObjectName("speed")
        self.horizontalLayout_2.addWidget(self.speed)
        self.pp = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.pp.setMaximumSize(QtCore.QSize(30, 30))
        self.pp.setObjectName("pp")
        self.horizontalLayout_2.addWidget(self.pp)
        self.prof = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.prof.setMaximumSize(QtCore.QSize(30, 30))
        self.prof.setObjectName("prof")
        self.horizontalLayout_2.addWidget(self.prof)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(200, 20, 221, 80))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 221, 73))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.str = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.str.setMaximumSize(QtCore.QSize(30, 50))
        self.str.setObjectName("str")
        self.horizontalLayout_3.addWidget(self.str)
        self.dex = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.dex.setMaximumSize(QtCore.QSize(30, 50))
        self.dex.setObjectName("dex")
        self.horizontalLayout_3.addWidget(self.dex)
        self.con = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.con.setMaximumSize(QtCore.QSize(30, 50))
        self.con.setObjectName("con")
        self.horizontalLayout_3.addWidget(self.con)
        self.int_ = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.int_.setMaximumSize(QtCore.QSize(30, 50))
        self.int_.setObjectName("int_")
        self.horizontalLayout_3.addWidget(self.int_)
        self.wis = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.wis.setMaximumSize(QtCore.QSize(30, 50))
        self.wis.setObjectName("wis")
        self.horizontalLayout_3.addWidget(self.wis)
        self.cha = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.cha.setMaximumSize(QtCore.QSize(30, 50))
        self.cha.setObjectName("cha")
        self.horizontalLayout_3.addWidget(self.cha)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 120, 261, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.skills = QtWidgets.QTextBrowser(self.groupBox_4)
        self.skills.setGeometry(QtCore.QRect(0, 15, 251, 101))
        self.skills.setObjectName("skills")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 110, 131, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.xp = QtWidgets.QTextBrowser(self.groupBox_5)
        self.xp.setGeometry(QtCore.QRect(10, 15, 110, 30))
        self.xp.setObjectName("xp")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(280, 160, 141, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.notes = QtWidgets.QTextBrowser(self.groupBox_6)
        self.notes.setGeometry(QtCore.QRect(0, 20, 141, 61))
        self.notes.setObjectName("notes")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 431, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.abilities = QtWidgets.QTextBrowser(self.groupBox_7)
        self.abilities.setGeometry(QtCore.QRect(0, 15, 211, 201))
        self.abilities.setObjectName("abilities")
        self.horizontalLayout.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.actions = QtWidgets.QTextBrowser(self.groupBox_8)
        self.actions.setGeometry(QtCore.QRect(0, 15, 211, 201))
        self.actions.setObjectName("actions")
        self.horizontalLayout.addWidget(self.groupBox_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Stats"))
        self.groupBox_3.setTitle(_translate("Form", "   HP      AC       speed     PP      Prof."))
        self.groupBox.setTitle(_translate("Form", "STR      DEX     CON      INT       WIS      CHA"))
        self.str.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.dex.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.con.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.int_.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.wis.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.cha.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("Form", "Skills"))
        self.groupBox_5.setTitle(_translate("Form", "XP"))
        self.xp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">50</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("Form", "Notes"))
        self.groupBox_7.setTitle(_translate("Form", "Abilities"))
        self.groupBox_8.setTitle(_translate("Form", "Actions"))