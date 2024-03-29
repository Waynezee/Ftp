# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FtpServer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
import threading
from multiprocessing import Process
import configparser
import logging
import os,sys
import Ftp_Server
import utils
import socket
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FtpServer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 8, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 7, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 7, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 6, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 2, 1, 4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 7, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 4, 1, 4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        self.menuFTP_Server = QtWidgets.QMenu(self.menubar)
        self.menuFTP_Server.setObjectName("menuFTP_Server")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFTP_Server.menuAction())
        self.pushButton_2.setEnabled(False)
        self.pushButton_6.setEnabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "最大连接数："))
        self.lineEdit.setText(_translate("MainWindow", "127.0.0.1"))
        self.lineEdit_3.setText(_translate("MainWindow", "100 "))
        self.pushButton_3.setText(_translate("MainWindow", "增加新用户"))
        self.pushButton.setText(_translate("MainWindow", "ON"))
        self.label_9.setText(_translate("MainWindow", "Mb/s"))
        self.label_11.setText(_translate("MainWindow", "确定端口可用"))
        self.label_4.setText(_translate("MainWindow", "端口:"))
        self.label.setText(_translate("MainWindow", "FTP_SERVER:"))
        self.lineEdit_4.setText(_translate("MainWindow", "100"))
        self.lineEdit_5.setText(_translate("MainWindow", "100"))
        self.label_2.setText(_translate("MainWindow", "匿名访问开关:"))
        self.label_3.setText(_translate("MainWindow", "IP:"))
        self.pushButton_5.setText(_translate("MainWindow", "OFF"))
        self.label_10.setText(_translate("MainWindow", "Mb/s"))
        self.pushButton_4.setText(_translate("MainWindow", "查看用户列表"))
        self.lineEdit_2.setText(_translate("MainWindow", "21"))
        self.pushButton_2.setText(_translate("MainWindow", "ON"))
        self.label_5.setText(_translate("MainWindow", "最大下载速度："))
        self.label_6.setText(_translate("MainWindow", "最大上载速度："))
        self.pushButton_6.setText(_translate("MainWindow", "OFF"))
        self.menuFTP_Server.setTitle(_translate("MainWindow", "FTP_Server"))
    def showDialog(self,str):
        vbox=QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        panel = QtWidgets.QLabel()
        panel.setText(str)
        self.dialog = QtWidgets.QDialog()
        self.dialog.resize(300,200)
        self.dialog.setWindowTitle("提示信息！")
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dialog.exec_()

               
def setstatus(ui,server_status,anon_status):
    if server_status == True:
        ui.pushButton.setEnabled(False)
        ui.pushButton_5.setEnabled(True)
        ui.pushButton_2.setEnabled(False)
        ui.pushButton_3.setEnabled(False)
        ui.pushButton_4.setEnabled(False)
        ui.pushButton_6.setEnabled(False)
        ui.lineEdit.setEnabled(False)
        ui .lineEdit_2.setEnabled(False)
        ui.lineEdit_3.setEnabled(False)
        ui.lineEdit_4.setEnabled(False)
        ui.lineEdit_5.setEnabled(False)
        ui.lineEdit_6.setEnabled(False)
    else:
        ui.pushButton.setEnabled(True)
        ui.pushButton_5.setEnabled(False)
        
        ui.pushButton_3.setEnabled(True)
        ui.pushButton_4.setEnabled(True)
        if anon_status==True:
            ui.pushButton_2.setEnabled(False)
            ui.pushButton_6.setEnabled(True)
        if anon_status==True:
            ui.pushButton_2.setEnabled(True)
            ui.pushButton_6.setEnabled(False)
        ui.lineEdit.setEnabled(True)
        ui.lineEdit_2.setEnabled(True)
        ui.lineEdit_3.setEnabled(True)
        ui.lineEdit_4.setEnabled(True)
        ui.lineEdit_5.setEnabled(True)
        ui.lineEdit_6.setEnabled(True)

class func(object):
    def __init__(self):
        self.num_th = 0
        self.nums = 100
        self.threads = []

def createThreads():
    for i in range(fun.nums):
        thread_ftp = threading.Thread(target=makeconnect,args=())
        thread_ftp.setDaemon(True)
        fun.threads.append(thread_ftp)
    return fun

def makeclose():
    utils.stop_thread(fun.threads[fun.num_th])
    setstatus(ui,False,True)
    fun.num_th += 1
    print("ftp_server close up")
def makeconnect():
    try:
        status = not ui.pushButton_2.isEnabled()
        setstatus(ui,True,status)
        ftp = Ftp_Server.FTP_server()
        ftp.ip = ui.lineEdit.text()
        ftp.port = ui.lineEdit_2.text()
        ftp.max_download = int(ui.lineEdit_3.text()) * 1024
        ftp.max_upload = int(ui.lineEdit_4.text()) * 1024
        ftp.max_cons = int(ui.lineEdit_5.text())
        ftp.max_pre_ip = 10
        if ui.pushButton_2.isEnabled():
            ftp.enable_anonymous = False
        if os.path.isdir(ui.lineEdit_6.text()):
            ftp.anonymous_dir = ui.lineEdit_6.text()
        ftp.startServer()
    except socket.error:
        pass
    print("ftp_server starting up")
def run():
    fun.threads[fun.num_th].start()

def OnChange():
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_6.setEnabled(True)    
def OffChange():
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_6.setEnabled(False)  

# for test 
def click_success():
    print("clicked success")
def connect():
    ui.pushButton.clicked.connect(partial(run))
    ui.pushButton_5.clicked.connect(partial(makeclose))
    ui.pushButton_2.clicked.connect(partial(OnChange))
    ui.pushButton_6.clicked.connect(partial(OffChange))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    fun = func()
    fun = createThreads()
    ui.setupUi(MainWindow)
    connect()
    MainWindow.show()    
    sys.exit(app.exec_())