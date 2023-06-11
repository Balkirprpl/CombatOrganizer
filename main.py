# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import addcreature, loadencounter

class Creature:
    name = ''
    hp = 0
    ac = 0
    speed = 0
    str_ = 0
    dex = 0
    con = 0
    int_ = 0
    wis = 0
    cha = 0
    prof = 0
    skills = []
    actions = []
    id = 0
    xp = 0

    def __init__(self, name, hp, ac, speed, str_, dex, con, int_, wis,char, prof, skills, actions, xp, notes):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.str_ = str_
        self.dex = dex
        self.con = con
        self.int_ = int_
        self.wis = wis
        self.cha = cha
        self.prof = prof
        self.id = len(characters)
        self.xp = xp
        self.notes = notes
        
class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QtCore.QSize(600, 300))
        Dialog.setMaximumSize(QtCore.QSize(600, 300))
        self.gridWidget = QtWidgets.QWidget(Dialog)
        self.gridWidget.setGeometry(QtCore.QRect(10, 10, 581, 271))
        self.gridWidget.setMinimumSize(QtCore.QSize(581, 271))
        self.gridWidget.setMaximumSize(QtCore.QSize(581, 271))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.gridWidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(185, 183))
        self.groupBox_4.setMaximumSize(QtCore.QSize(185, 183))
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget.setGeometry(QtCore.QRect(0, 15, 185, 161))
        self.listWidget.setMinimumSize(QtCore.QSize(185, 161))
        self.listWidget.setMaximumSize(QtCore.QSize(185, 161))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridWidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(185, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(185, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 15, 170, 23))
        self.textBrowser.setMinimumSize(QtCore.QSize(170, 23))
        self.textBrowser.setMaximumSize(QtCore.QSize(170, 23))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 49, 70, 23))
        self.comboBox.setMinimumSize(QtCore.QSize(70, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(70, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.sendbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.sendbutton.setGeometry(QtCore.QRect(110, 50, 70, 23))
        self.sendbutton.setMinimumSize(QtCore.QSize(70, 23))
        self.sendbutton.setMaximumSize(QtCore.QSize(70, 23))
        self.sendbutton.setObjectName("sendbutton")
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridWidget)
        self.widget.setMinimumSize(QtCore.QSize(185, 80))
        self.widget.setMaximumSize(QtCore.QSize(185, 80))
        self.widget.setObjectName("widget")
        self.gridGroupBox = QtWidgets.QGroupBox(self.widget)
        self.gridGroupBox.setGeometry(QtCore.QRect(0, 0, 189, 80))
        self.gridGroupBox.setMinimumSize(QtCore.QSize(189, 80))
        self.gridGroupBox.setMaximumSize(QtCore.QSize(189, 80))
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.damagebutton = QtWidgets.QPushButton(self.gridGroupBox)
        self.damagebutton.setMinimumSize(QtCore.QSize(185, 30))
        self.damagebutton.setMaximumSize(QtCore.QSize(185, 30))
        self.damagebutton.setObjectName("damagebutton")
        self.gridLayout_2.addWidget(self.damagebutton, 0, 0, 1, 1)
        self.addcreaturebutton = QtWidgets.QPushButton(self.gridGroupBox)
        self.addcreaturebutton.setMinimumSize(QtCore.QSize(90, 23))
        self.addcreaturebutton.setMaximumSize(QtCore.QSize(90, 23))
        self.addcreaturebutton.setObjectName("addcreaturebutton")
        self.gridLayout_2.addWidget(self.addcreaturebutton, 1, 0, 1, 1)
        self.loadencounterbutton = QtWidgets.QPushButton(self.gridGroupBox)
        self.loadencounterbutton.setMinimumSize(QtCore.QSize(83, 23))
        self.loadencounterbutton.setMaximumSize(QtCore.QSize(83, 23))
        self.loadencounterbutton.setObjectName("loadencounterbutton")
        self.gridLayout_2.addWidget(self.loadencounterbutton, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 3, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gridWidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(185, 183))
        self.groupBox_3.setMaximumSize(QtCore.QSize(185, 183))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 14, 161, 161))
        self.textBrowser_2.setMinimumSize(QtCore.QSize(161, 161))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(161, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(197, 269))
        self.groupBox.setMaximumSize(QtCore.QSize(197, 269))
        self.groupBox.setObjectName("groupBox")
        self.listView_3 = QtWidgets.QListView(self.groupBox)
        self.listView_3.setGeometry(QtCore.QRect(0, 20, 191, 241))
        self.listView_3.setMinimumSize(QtCore.QSize(191, 241))
        self.listView_3.setMaximumSize(QtCore.QSize(191, 241))
        self.listView_3.setObjectName("listView_3")
        self.gridLayout.addWidget(self.groupBox, 0, 2, 4, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def open_addcreature():
            self.Dialog = QtWidgets.QDialog()
            self.ui = addcreature.Ui_Dialog()
            self.ui.setupUi(self.Dialog)
            self.ui.pushButton.clicked.connect(add_creature)
            self.Dialog.show()
        
        def open_loadencounter():
            self.Dialog = QtWidgets.QDialog()
            self.ui = loadencounter.Ui_Dialog()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()

        def open_damage():
            print('damage')

        def add_creature():
            print("correct")
            creature = Creature(self.ui.name.toPlainText(),self.ui.hp.toPlainText(),self.ui.ac.toPlainText(),self.ui.speed.toPlainText(), self.ui.str.toPlainText(), self.ui.dex.toPlainText(), self.ui.con.toPlainText(), self.ui.int_2.toPlainText(),self.ui.wis.toPlainText(),self.ui.cha.toPlainText(),self.ui.prof.toPlainText(),self.ui.pp.toPlainText(),self.ui.xp.toPlainText(),self.ui.skills.toPlainText(),self.ui.notes.toPlainText(),self.ui.abilities.toPlainText(),self.ui.actions.toPlainText())
            

        
            
        self.damagebutton.clicked.connect(open_damage)
        self.addcreaturebutton.clicked.connect(open_addcreature)
        self.loadencounterbutton.clicked.connect(open_loadencounter)
        #self.sendbutton.clicked.connect(send)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_4.setTitle(_translate("Dialog", "Loaded creatures"))
        self.groupBox_2.setTitle(_translate("Dialog", "Initiative"))
        self.textBrowser.setPlaceholderText(_translate("Dialog", "Creature"))
        self.comboBox.setItemText(0, _translate("Dialog", "1"))
        self.comboBox.setItemText(1, _translate("Dialog", "2"))
        self.comboBox.setItemText(2, _translate("Dialog", "3"))
        self.comboBox.setItemText(3, _translate("Dialog", "4"))
        self.comboBox.setItemText(4, _translate("Dialog", "5"))
        self.comboBox.setItemText(5, _translate("Dialog", "6"))
        self.comboBox.setItemText(6, _translate("Dialog", "7"))
        self.comboBox.setItemText(7, _translate("Dialog", "8"))
        self.comboBox.setItemText(8, _translate("Dialog", "9"))
        self.comboBox.setItemText(9, _translate("Dialog", "10"))
        self.comboBox.setItemText(10, _translate("Dialog", "11"))
        self.comboBox.setItemText(11, _translate("Dialog", "12"))
        self.comboBox.setItemText(12, _translate("Dialog", "13"))
        self.comboBox.setItemText(13, _translate("Dialog", "14"))
        self.comboBox.setItemText(14, _translate("Dialog", "15"))
        self.comboBox.setItemText(15, _translate("Dialog", "16"))
        self.comboBox.setItemText(16, _translate("Dialog", "17"))
        self.comboBox.setItemText(17, _translate("Dialog", "18"))
        self.comboBox.setItemText(18, _translate("Dialog", "19"))
        self.comboBox.setItemText(19, _translate("Dialog", "20"))
        self.comboBox.setItemText(20, _translate("Dialog", "21"))
        self.comboBox.setItemText(21, _translate("Dialog", "22"))
        self.comboBox.setItemText(22, _translate("Dialog", "23"))
        self.comboBox.setItemText(23, _translate("Dialog", "24"))
        self.comboBox.setItemText(24, _translate("Dialog", "25"))
        self.sendbutton.setText(_translate("Dialog", "Send"))
        self.damagebutton.setText(_translate("Dialog", "Deal damage"))
        self.addcreaturebutton.setText(_translate("Dialog", "Load creature"))
        self.loadencounterbutton.setText(_translate("Dialog", "Load encounter"))
        self.groupBox_3.setTitle(_translate("Dialog", "Stats"))
        self.groupBox.setTitle(_translate("Dialog", "Initiative"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
