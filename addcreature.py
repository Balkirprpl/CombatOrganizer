# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcreature.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setMinimumSize(QtCore.QSize(500, 500))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 181))
        self.groupBox.setMinimumSize(QtCore.QSize(491, 181))
        self.groupBox.setMaximumSize(QtCore.QSize(491, 181))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 161))
        self.verticalLayoutWidget.setMaximumSize(QtCore.QSize(160, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.name.setMinimumSize(QtCore.QSize(158, 36))
        self.name.setMaximumSize(QtCore.QSize(158, 36))
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.hp = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.hp.setMinimumSize(QtCore.QSize(158, 35))
        self.hp.setMaximumSize(QtCore.QSize(158, 35))
        self.hp.setObjectName("hp")
        self.verticalLayout.addWidget(self.hp)
        self.ac = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.ac.setMinimumSize(QtCore.QSize(158, 35))
        self.ac.setMaximumSize(QtCore.QSize(158, 35))
        self.ac.setObjectName("ac")
        self.verticalLayout.addWidget(self.ac)
        self.speed = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.speed.setMinimumSize(QtCore.QSize(158, 35))
        self.speed.setMaximumSize(QtCore.QSize(158, 35))
        self.speed.setObjectName("speed")
        self.verticalLayout.addWidget(self.speed)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 20, 301, 51))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(301, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.str = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.str.setMaximumSize(QtCore.QSize(45, 49))
        self.str.setObjectName("str")
        self.horizontalLayout.addWidget(self.str)
        self.dex = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.dex.setMaximumSize(QtCore.QSize(45, 49))
        self.dex.setObjectName("dex")
        self.horizontalLayout.addWidget(self.dex)
        self.con = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.con.setMaximumSize(QtCore.QSize(45, 49))
        self.con.setObjectName("con")
        self.horizontalLayout.addWidget(self.con)
        self.int_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.int_2.setMaximumSize(QtCore.QSize(45, 49))
        self.int_2.setObjectName("int_2")
        self.horizontalLayout.addWidget(self.int_2)
        self.wis = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.wis.setMaximumSize(QtCore.QSize(45, 49))
        self.wis.setObjectName("wis")
        self.horizontalLayout.addWidget(self.wis)
        self.cha = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.cha.setObjectName("cha")
        self.horizontalLayout.addWidget(self.cha)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(180, 110, 301, 41))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prof = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.prof.setMinimumSize(QtCore.QSize(100, 0))
        self.prof.setMaximumSize(QtCore.QSize(100, 39))
        self.prof.setObjectName("prof")
        self.horizontalLayout_2.addWidget(self.prof)
        self.pp = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.pp.setMinimumSize(QtCore.QSize(100, 0))
        self.pp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pp.setObjectName("pp")
        self.horizontalLayout_2.addWidget(self.pp)
        self.xp = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.xp.setMinimumSize(QtCore.QSize(100, 0))
        self.xp.setMaximumSize(QtCore.QSize(100, 39))
        self.xp.setObjectName("xp")
        self.horizontalLayout_2.addWidget(self.xp)
        self.horizontalWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_3.setGeometry(QtCore.QRect(10, 210, 480, 96))
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.skills = QtWidgets.QTextEdit(self.horizontalWidget_3)
        self.skills.setMaximumSize(QtCore.QSize(160, 78))
        self.skills.setObjectName("skills")
        self.horizontalLayout_3.addWidget(self.skills)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 78))
        self.pushButton.setMaximumSize(QtCore.QSize(160, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.notes = QtWidgets.QTextEdit(self.horizontalWidget_3)
        self.notes.setMaximumSize(QtCore.QSize(160, 78))
        self.notes.setObjectName("notes")
        self.horizontalLayout_3.addWidget(self.notes)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 310, 481, 181))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.abilities = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.abilities.setObjectName("abilities")
        self.horizontalLayout_4.addWidget(self.abilities)
        self.actions = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.actions.setObjectName("actions")
        self.horizontalLayout_4.addWidget(self.actions)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name.setPlaceholderText(_translate("Dialog", "Name"))
        self.hp.setPlaceholderText(_translate("Dialog", "HP"))
        self.ac.setPlaceholderText(_translate("Dialog", "AC"))
        self.speed.setPlaceholderText(_translate("Dialog", "SPEED"))
        self.str.setPlaceholderText(_translate("Dialog", "STR"))
        self.dex.setPlaceholderText(_translate("Dialog", "DEX"))
        self.con.setPlaceholderText(_translate("Dialog", "CON"))
        self.int_2.setPlaceholderText(_translate("Dialog", "INT"))
        self.wis.setPlaceholderText(_translate("Dialog", "WIS"))
        self.cha.setPlaceholderText(_translate("Dialog", "CHA"))
        self.prof.setPlaceholderText(_translate("Dialog", "Proficiency"))
        self.pp.setPlaceholderText(_translate("Dialog", "Passive Perception"))
        self.xp.setPlaceholderText(_translate("Dialog", "XP"))
        self.skills.setPlaceholderText(_translate("Dialog", "Skills (Eg: stealth +6, Blinded, Blindsight 30ft...)"))
        self.pushButton.setText(_translate("Dialog", "Create"))
        self.notes.setPlaceholderText(_translate("Dialog", "Notes"))
        self.abilities.setPlaceholderText(_translate("Dialog", "Abilities"))
        self.actions.setPlaceholderText(_translate("Dialog", "Actions"))
