# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SerialCom
from invKin import *

class Ui_ArmControl(object):
    def setupUi(self, ArmControl):
        ArmControl.setObjectName("ArmControl")
        ArmControl.setWindowModality(QtCore.Qt.NonModal)
        ArmControl.resize(482, 537)
        ArmControl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../roboticArm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ArmControl.setWindowIcon(icon)
        ArmControl.setWindowOpacity(1.0)
        ArmControl.setAutoFillBackground(False)
        self.xUp = QtWidgets.QPushButton(ArmControl)
        self.xUp.setGeometry(QtCore.QRect(360, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.xUp.setFont(font)
        self.xUp.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.xUp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xUp.setIcon(icon1)
        self.xUp.setIconSize(QtCore.QSize(32, 32))
        self.xUp.setFlat(True)
        self.xUp.setObjectName("xUp")
        self.xVal = QtWidgets.QLabel(ArmControl)
        self.xVal.setGeometry(QtCore.QRect(260, 130, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.xVal.setFont(font)
        self.xVal.setFrameShape(QtWidgets.QFrame.Box)
        self.xVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.xVal.setLineWidth(1)
        self.xVal.setMidLineWidth(0)
        self.xVal.setAlignment(QtCore.Qt.AlignCenter)
        self.xVal.setWordWrap(False)
        self.xVal.setObjectName("xVal")
        self.yVal = QtWidgets.QLabel(ArmControl)
        self.yVal.setGeometry(QtCore.QRect(260, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.yVal.setFont(font)
        self.yVal.setFrameShape(QtWidgets.QFrame.Box)
        self.yVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yVal.setLineWidth(1)
        self.yVal.setMidLineWidth(0)
        self.yVal.setAlignment(QtCore.Qt.AlignCenter)
        self.yVal.setWordWrap(False)
        self.yVal.setObjectName("yVal")
        self.rollVal = QtWidgets.QLabel(ArmControl)
        self.rollVal.setGeometry(QtCore.QRect(260, 310, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.rollVal.setFont(font)
        self.rollVal.setFrameShape(QtWidgets.QFrame.Box)
        self.rollVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rollVal.setLineWidth(1)
        self.rollVal.setMidLineWidth(0)
        self.rollVal.setAlignment(QtCore.Qt.AlignCenter)
        self.rollVal.setWordWrap(False)
        self.rollVal.setObjectName("rollVal")
        self.zVal = QtWidgets.QLabel(ArmControl)
        self.zVal.setGeometry(QtCore.QRect(260, 250, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.zVal.setFont(font)
        self.zVal.setFrameShape(QtWidgets.QFrame.Box)
        self.zVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zVal.setLineWidth(1)
        self.zVal.setMidLineWidth(0)
        self.zVal.setAlignment(QtCore.Qt.AlignCenter)
        self.zVal.setWordWrap(False)
        self.zVal.setObjectName("zVal")
        self.xLabel = QtWidgets.QLabel(ArmControl)
        self.xLabel.setGeometry(QtCore.QRect(80, 130, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.xLabel.setFont(font)
        self.xLabel.setAutoFillBackground(False)
        self.xLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.xLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.xLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.xLabel.setLineWidth(1)
        self.xLabel.setMidLineWidth(0)
        self.xLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xLabel.setWordWrap(False)
        self.xLabel.setObjectName("xLabel")
        self.yUp = QtWidgets.QPushButton(ArmControl)
        self.yUp.setGeometry(QtCore.QRect(360, 190, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.yUp.setFont(font)
        self.yUp.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.yUp.setText("")
        self.yUp.setIcon(icon1)
        self.yUp.setIconSize(QtCore.QSize(32, 32))
        self.yUp.setFlat(True)
        self.yUp.setObjectName("yUp")
        self.rollup = QtWidgets.QPushButton(ArmControl)
        self.rollup.setGeometry(QtCore.QRect(360, 310, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.rollup.setFont(font)
        self.rollup.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.rollup.setText("")
        self.rollup.setIcon(icon1)
        self.rollup.setIconSize(QtCore.QSize(32, 32))
        self.rollup.setFlat(True)
        self.rollup.setObjectName("rollup")
        self.zUp = QtWidgets.QPushButton(ArmControl)
        self.zUp.setGeometry(QtCore.QRect(360, 250, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.zUp.setFont(font)
        self.zUp.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.zUp.setText("")
        self.zUp.setIcon(icon1)
        self.zUp.setIconSize(QtCore.QSize(32, 32))
        self.zUp.setFlat(True)
        self.zUp.setObjectName("zUp")
        self.xDown = QtWidgets.QPushButton(ArmControl)
        self.xDown.setGeometry(QtCore.QRect(200, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.xDown.setFont(font)
        self.xDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.xDown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xDown.setIcon(icon2)
        self.xDown.setIconSize(QtCore.QSize(32, 32))
        self.xDown.setFlat(True)
        self.xDown.setObjectName("xDown")
        self.yDown = QtWidgets.QPushButton(ArmControl)
        self.yDown.setGeometry(QtCore.QRect(200, 190, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.yDown.setFont(font)
        self.yDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.yDown.setText("")
        self.yDown.setIcon(icon2)
        self.yDown.setIconSize(QtCore.QSize(32, 32))
        self.yDown.setFlat(True)
        self.yDown.setObjectName("yDown")
        self.zDown = QtWidgets.QPushButton(ArmControl)
        self.zDown.setGeometry(QtCore.QRect(200, 250, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.zDown.setFont(font)
        self.zDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.zDown.setText("")
        self.zDown.setIcon(icon2)
        self.zDown.setIconSize(QtCore.QSize(32, 32))
        self.zDown.setFlat(True)
        self.zDown.setObjectName("zDown")
        self.rollDown = QtWidgets.QPushButton(ArmControl)
        self.rollDown.setGeometry(QtCore.QRect(200, 310, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.rollDown.setFont(font)
        self.rollDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.rollDown.setText("")
        self.rollDown.setIcon(icon2)
        self.rollDown.setIconSize(QtCore.QSize(32, 32))
        self.rollDown.setFlat(True)
        self.rollDown.setObjectName("rollDown")
        self.yLabel = QtWidgets.QLabel(ArmControl)
        self.yLabel.setGeometry(QtCore.QRect(80, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.yLabel.setFont(font)
        self.yLabel.setAutoFillBackground(False)
        self.yLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.yLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.yLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yLabel.setLineWidth(1)
        self.yLabel.setMidLineWidth(0)
        self.yLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yLabel.setWordWrap(False)
        self.yLabel.setObjectName("yLabel")
        self.zLabel = QtWidgets.QLabel(ArmControl)
        self.zLabel.setGeometry(QtCore.QRect(80, 250, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.zLabel.setFont(font)
        self.zLabel.setAutoFillBackground(False)
        self.zLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.zLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.zLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zLabel.setLineWidth(1)
        self.zLabel.setMidLineWidth(0)
        self.zLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zLabel.setWordWrap(False)
        self.zLabel.setObjectName("zLabel")
        self.rollLabel = QtWidgets.QLabel(ArmControl)
        self.rollLabel.setGeometry(QtCore.QRect(80, 310, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.rollLabel.setFont(font)
        self.rollLabel.setAutoFillBackground(False)
        self.rollLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.rollLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.rollLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rollLabel.setLineWidth(1)
        self.rollLabel.setMidLineWidth(0)
        self.rollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rollLabel.setWordWrap(False)
        self.rollLabel.setObjectName("rollLabel")
        self.titleLabel = QtWidgets.QLabel(ArmControl)
        self.titleLabel.setGeometry(QtCore.QRect(30, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.sendButton = QtWidgets.QPushButton(ArmControl)
        self.sendButton.setGeometry(QtCore.QRect(350, 30, 41, 51))
        self.sendButton.setText("")
        self.sendButton.setIcon(icon)
        self.sendButton.setIconSize(QtCore.QSize(32, 32))
        self.sendButton.setFlat(True)
        self.sendButton.setObjectName("sendButton")
        self.closeButton = QtWidgets.QPushButton(ArmControl)
        self.closeButton.setGeometry(QtCore.QRect(400, 30, 51, 51))
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../closeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(48, 48))
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.pitchVal = QtWidgets.QLabel(ArmControl)
        self.pitchVal.setGeometry(QtCore.QRect(260, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.pitchVal.setFont(font)
        self.pitchVal.setFrameShape(QtWidgets.QFrame.Box)
        self.pitchVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pitchVal.setLineWidth(1)
        self.pitchVal.setMidLineWidth(0)
        self.pitchVal.setAlignment(QtCore.Qt.AlignCenter)
        self.pitchVal.setWordWrap(False)
        self.pitchVal.setObjectName("pitchVal")
        self.pitchDown = QtWidgets.QPushButton(ArmControl)
        self.pitchDown.setGeometry(QtCore.QRect(200, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.pitchDown.setFont(font)
        self.pitchDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.pitchDown.setText("")
        self.pitchDown.setIcon(icon2)
        self.pitchDown.setIconSize(QtCore.QSize(32, 32))
        self.pitchDown.setFlat(True)
        self.pitchDown.setObjectName("pitchDown")
        self.pitchLabel = QtWidgets.QLabel(ArmControl)
        self.pitchLabel.setGeometry(QtCore.QRect(80, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.pitchLabel.setFont(font)
        self.pitchLabel.setAutoFillBackground(False)
        self.pitchLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.pitchLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.pitchLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pitchLabel.setLineWidth(1)
        self.pitchLabel.setMidLineWidth(0)
        self.pitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pitchLabel.setWordWrap(False)
        self.pitchLabel.setObjectName("pitchLabel")
        self.pitchUp = QtWidgets.QPushButton(ArmControl)
        self.pitchUp.setGeometry(QtCore.QRect(360, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.pitchUp.setFont(font)
        self.pitchUp.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.pitchUp.setText("")
        self.pitchUp.setIcon(icon1)
        self.pitchUp.setIconSize(QtCore.QSize(32, 32))
        self.pitchUp.setFlat(True)
        self.pitchUp.setObjectName("pitchUp")
        self.yawVal = QtWidgets.QLabel(ArmControl)
        self.yawVal.setGeometry(QtCore.QRect(260, 430, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(14)
        self.yawVal.setFont(font)
        self.yawVal.setFrameShape(QtWidgets.QFrame.Box)
        self.yawVal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yawVal.setLineWidth(1)
        self.yawVal.setMidLineWidth(0)
        self.yawVal.setAlignment(QtCore.Qt.AlignCenter)
        self.yawVal.setWordWrap(False)
        self.yawVal.setObjectName("yawVal")
        self.yawDown = QtWidgets.QPushButton(ArmControl)
        self.yawDown.setGeometry(QtCore.QRect(200, 430, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.yawDown.setFont(font)
        self.yawDown.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.yawDown.setText("")
        self.yawDown.setIcon(icon2)
        self.yawDown.setIconSize(QtCore.QSize(32, 32))
        self.yawDown.setFlat(True)
        self.yawDown.setObjectName("yawDown")
        self.yawLabel = QtWidgets.QLabel(ArmControl)
        self.yawLabel.setGeometry(QtCore.QRect(80, 430, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.yawLabel.setFont(font)
        self.yawLabel.setAutoFillBackground(False)
        self.yawLabel.setStyleSheet("background-color: rgb(237, 255, 248)")
        self.yawLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.yawLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yawLabel.setLineWidth(1)
        self.yawLabel.setMidLineWidth(0)
        self.yawLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yawLabel.setWordWrap(False)
        self.yawLabel.setObjectName("yawLabel")
        self.yawUp = QtWidgets.QPushButton(ArmControl)
        self.yawUp.setGeometry(QtCore.QRect(360, 430, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(16)
        self.yawUp.setFont(font)
        self.yawUp.setStyleSheet("color : rgb(255, 255, 255);\n"
"")
        self.yawUp.setText("")
        self.yawUp.setIcon(icon1)
        self.yawUp.setIconSize(QtCore.QSize(32, 32))
        self.yawUp.setFlat(True)
        self.yawUp.setObjectName("yawUp")
        self.subtitleLabel = QtWidgets.QLabel(ArmControl)
        self.subtitleLabel.setGeometry(QtCore.QRect(190, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setObjectName("subtitleLabel")

        self.retranslateUi(ArmControl)
        QtCore.QMetaObject.connectSlotsByName(ArmControl)

    def retranslateUi(self, ArmControl):
        _translate = QtCore.QCoreApplication.translate
        ArmControl.setWindowTitle(_translate("ArmControl", "Arm Control"))
        self.xVal.setText(_translate("ArmControl", "0.4"))
        self.yVal.setText(_translate("ArmControl", "1.3"))
        self.rollVal.setText(_translate("ArmControl", "1"))
        self.zVal.setText(_translate("ArmControl", "3"))
        self.xLabel.setText(_translate("ArmControl", "x"))
        self.yLabel.setText(_translate("ArmControl", "y"))
        self.zLabel.setText(_translate("ArmControl", "z"))
        self.rollLabel.setText(_translate("ArmControl", "roll"))
        self.titleLabel.setText(_translate("ArmControl", "Arm Control"))
        self.pitchVal.setText(_translate("ArmControl", "-1"))
        self.pitchLabel.setText(_translate("ArmControl", "pitch"))
        self.yawVal.setText(_translate("ArmControl", "-1"))
        self.yawLabel.setText(_translate("ArmControl", "yaw"))
        self.subtitleLabel.setText(_translate("ArmControl", "Team Avijatrik"))
        self.closeButton.clicked.connect(ArmControl.close)
        self.sendButton.clicked.connect(self.send)
        self.xDown.clicked.connect(self.xDownMethod)
        self.xUp.clicked.connect(self.xUpMethod)
        self.yDown.clicked.connect(self.yDownMethod)
        self.yUp.clicked.connect(self.yUpMethod)
        self.zDown.clicked.connect(self.zDownMethod)
        self.zUp.clicked.connect(self.zUpMethod)
        self.rollDown.clicked.connect(self.rollDownMethod)
        self.rollup.clicked.connect(self.rollupMethod)
        self.pitchDown.clicked.connect(self.pitchDownMethod)
        self.pitchUp.clicked.connect(self.pitchUpMethod)
        self.yawDown.clicked.connect(self.yawDownMethod)
        self.yawUp.clicked.connect(self.yawUpMethod)
        self.window = ArmControl

    def send(self):
        data = []
        val = int(self.xVal.text())
        data.append(str(val))
        val = int(self.yVal.text())
        data.append(str(val))
        val = int(self.zVal.text())
        data.append(str(val))
        val = int(self.rollVal.text())
        data.append(str(val))
        val = int(self.pitchVal.text())
        data.append(str(val))
        val = int(self.yawVal.text())
        data.append(str(val))
        dataString = ','.join(data)
        #self.window.SerialObj.sendString(dataString)
        print(dataString)
    
    
    def plot_data(self):

        px = float(self.xVal.text())
        py = float(self.yVal.text())
        pz = float(self.zVal.text())
        roll = float(self.rollVal.text())
        pitch = float(self.pitchVal.text())
        yaw = float(self.yawVal.text())
        q1,q2,q3,q4,q5,q6 = get_angles(px,py,pz,roll,pitch,yaw)
        X,Y,Z = forward_kin(q1,q2,q3,q4,q5,q6)
        update_plot(X,Y,Z,self.window.fig,self.window.ax)
    
    
    def xUpMethod(self):
        val = float(self.xVal.text())
        if(val<2):
                val+=.1
                self.xVal.setText(str(round(val,2))) 
                self.plot_data()
    def xDownMethod(self):
        val = float(self.xVal.text())
        if(val>0):
                val -= .1
                self.xVal.setText(str(round(val,2)))
                self.plot_data()

   
    def yUpMethod(self):
        val = float(self.yVal.text())
        if(val<3):
                val+=.1
                self.yVal.setText(str(round(val,2)))
                self.plot_data()
    def yDownMethod(self):
        val = float(self.yVal.text())
        if(val>0):
                val -= .1
                self.yVal.setText(str(round(val,2)))
                self.plot_data()
  
  
    def zUpMethod(self):
        val = float(self.zVal.text())
        if(val<5):
                val+=.1
                self.zVal.setText(str(round(val,2)))
                self.plot_data()
    def zDownMethod(self):
        val = float(self.zVal.text())
        if(val>0):
                val -= .1
                self.zVal.setText(str(round(val,2)))
                self.plot_data()

    def rollupMethod(self):
        val = float(self.rollVal.text())
        if(val<3.14):
                val+=.1
                self.rollVal.setText(str(round(val,2)))
                self.plot_data()
    def rollDownMethod(self):
        val = float(self.rollVal.text())
        if(val>-3.14):
                val -= .1
                self.rollVal.setText(str(round(val,2)))
                self.plot_data()    

    def pitchUpMethod(self):
        val = float(self.pitchVal.text())
        if(val<3.14):
                val+=.1
                self.pitchVal.setText(str(round(val,2)))
                self.plot_data()
    def pitchDownMethod(self):
        val = float(self.pitchVal.text())
        if(val>-3.14):
                val -= .1
                self.pitchVal.setText(str(round(val,2)))
                self.plot_data()  
    def yawUpMethod(self):
        val = float(self.yawVal.text())
        if(val<3.14):
                val+=.1
                self.yawVal.setText(str(round(val,2)))
                self.plot_data()
    def yawDownMethod(self):
        val = float(self.yawVal.text())
        if(val>-3.14):
                val -= .1
                self.yawVal.setText(str(round(val,2)))
                self.plot_data()  
    
    


class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitSerial()
        self.InitPlot()

    def InitPlot(self):
        self.fig,self.ax = create_plot()
        


    def InitSerial(self):
        #self.SerialObj = SerialCom.SerialCom()
        #self.arduinoOut = self.SerialObj.getConn('COM9',9600) 
        pass
    def close(self):
        sys.exit()
    



def main():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = Main_window()
        ui = Ui_ArmControl()
        ui.setupUi(MainWindow)
        MainWindow.show()
        plt.show()
        sys.exit(app.exec_())
        


if __name__ == "__main__":
        main()

