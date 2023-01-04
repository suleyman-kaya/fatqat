# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FatqatMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import socket, time
from PyQt5 import QtCore, QtGui, QtWidgets
from dronekit import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal



class Ui_FatqatMainWindow(object):
    def setupUi(self, FatqatMainWindow):
        FatqatMainWindow.setObjectName("FatqatMainWindow")
        FatqatMainWindow.resize(718, 524)
        self.centralwidget = QtWidgets.QWidget(FatqatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConnectionString_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ConnectionString_Textbox.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.ConnectionString_Textbox.setObjectName("ConnectionString_Textbox")
        self.Btn_Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Connect.setGeometry(QtCore.QRect(180, 10, 89, 25))
        self.Btn_Connect.setObjectName("Btn_Connect")
        self.VehicleStateTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.VehicleStateTextbox.setGeometry(QtCore.QRect(10, 90, 261, 221))
        self.VehicleStateTextbox.setObjectName("VehicleStateTextbox")
        self.ConnectionStatusTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.ConnectionStatusTextLabel.setGeometry(QtCore.QRect(10, 40, 131, 17))
        self.ConnectionStatusTextLabel.setObjectName("ConnectionStatusTextLabel")
        self.ConnectionStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ConnectionStatusLabel.setGeometry(QtCore.QRect(140, 40, 131, 17))
        self.ConnectionStatusLabel.setObjectName("ConnectionStatusLabel")
        self.VehicleStateLabel = QtWidgets.QLabel(self.centralwidget)
        self.VehicleStateLabel.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.VehicleStateLabel.setObjectName("VehicleStateLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 310, 261, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Altitude_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Altitude_Textbox.setGeometry(QtCore.QRect(80, 330, 113, 25))
        self.Altitude_Textbox.setObjectName("Altitude_Textbox")
        self.AltitudeLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeLabel.setGeometry(QtCore.QRect(10, 332, 67, 20))
        self.AltitudeLabel.setObjectName("AltitudeLabel")
        self.TakeOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.TakeOffButton.setGeometry(QtCore.QRect(200, 330, 71, 25))
        self.TakeOffButton.setObjectName("TakeOffButton")
        self.ArmAndTakeoffLogsTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ArmAndTakeoffLogsTextbox.setGeometry(QtCore.QRect(10, 360, 261, 111))
        self.ArmAndTakeoffLogsTextbox.setObjectName("ArmAndTakeoffLogsTextbox")
        FatqatMainWindow.setCentralWidget(self.centralwidget)
        FatqatMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FatqatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 22))
        self.menubar.setObjectName("menubar")
        FatqatMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FatqatMainWindow)
        self.statusbar.setObjectName("statusbar")
        FatqatMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FatqatMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FatqatMainWindow)

        self.Btn_Connect.clicked.connect(self.dkConect)
        self.TakeOffButton.clicked.connect(self.dkTakeOff)

    def retranslateUi(self, FatqatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FatqatMainWindow.setWindowTitle(_translate("FatqatMainWindow", "Fatqat - Ground Control Station Software"))
        self.Btn_Connect.setText(_translate("FatqatMainWindow", "Connect!"))
        self.ConnectionStatusTextLabel.setText(_translate("FatqatMainWindow", "Connection Status:"))
        self.ConnectionStatusLabel.setText(_translate("FatqatMainWindow", "Not Connected"))
        self.VehicleStateLabel.setText(_translate("FatqatMainWindow", "Vehicle State:"))
        self.AltitudeLabel.setText(_translate("FatqatMainWindow", "Altitude:"))
        self.TakeOffButton.setText(_translate("FatqatMainWindow", "Take-off!"))

    def dkConect(self):
        # bu fonksiyon dronekit kullanarak ConnectionString_Textbox.text()'teki text verisiyle ve wait_ready=True parametresiyle drone'a bağlanacak.
        cs = self.ConnectionString_Textbox.text()
        global vehicle
        try:
            global connectionStatus
            vehicle = connect(cs, wait_ready=True)
            self.dkGetVehicleState()
            connectionStatus = "Connected."
            self.ConnectionStatusLabel.setText("Connected.")
        except socket.error:
            connectionStatus = "No server exist!"
            self.ConnectionStatusLabel.setText(connectionStatus)
            print(connectionStatus)
        except OSError as e:
            connectionStatus = "No serial exist!"
            self.ConnectionStatusLabel.setText(connectionStatus)
        except APIException:
            connectionStatus = "Timeout!"
            self.ConnectionStatusLabel.setText(connectionStatus)
        except:
            connectionStatus = "Some other error!"
            self.ConnectionStatusLabel.setText(connectionStatus)

         
    def dkGetVehicleState(self):
        # bu fonksiyon dronekit kullanarak aracın durum bilgisini vehicleStateText (string) isimli bir değişkene kaydedecek ve bu değişkeni VehicleStateTextbox'a bastıracak.
        a= "Autopilot Firmware version: %s" % vehicle.version
        b= "Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp
        c= "Global Location: %s" % vehicle.location.global_frame
        d= "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
        e= "Local Location: %s" % vehicle.location.local_frame
        f= "Attitude: %s" % vehicle.attitude
        g= "Velocity: %s" % vehicle.velocity
        h= "GPS: %s" % vehicle.gps_0
        i= "Groundspeed: %s" % vehicle.groundspeed
        j= "Airspeed: %s" % vehicle.airspeed
        k= "Gimbal status: %s" % vehicle.gimbal
        l= "Battery: %s" % vehicle.battery
        m= "EKF OK?: %s" % vehicle.ekf_ok
        n= "Last Heartbeat: %s" % vehicle.last_heartbeat
        o= "Rangefinder: %s" % vehicle.rangefinder
        p= "Rangefinder distance: %s" % vehicle.rangefinder.distance
        r= "Rangefinder voltage: %s" % vehicle.rangefinder.voltage
        s= "Heading: %s" % vehicle.heading
        t= "Is Armable?: %s" % vehicle.is_armable
        u= "System status: %s" % vehicle.system_status.state
        v= "Mode: %s" % vehicle.mode.name
        y= "Armed: %s" % vehicle.armed

        global vehicleState
        vehicleState = a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+l+"\n"+m+"\n"+n+"\n"+o+"\n"+p+"\n"+r+"\n"+s+"\n"+t+"\n"+u+"\n"+v+"\n"+y

        self.VehicleStateTextbox.setPlainText(vehicleState)

        print(vehicleState)

    def arm_and_takeoff(self, aTargetAltitude):
        """
        Arms vehicle and fly to aTargetAltitude.
        """

        print("Basic pre-arm checks")
        # Don't try to arm until autopilot is ready
        while not vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)

        print("Arming motors")
        # Copter should arm in GUIDED mode
        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True
        while not vehicle.mode.name=='GUIDED' and not vehicle.armed:
            vehicle.mode = "GUIDED"
            time.sleep(1)

        # Confirm vehicle armed before attempting to take off
        while not vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)

        print("Taking off!")
        vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

        # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
        #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            print(" Altitude: ", vehicle.location.global_relative_frame.alt)
            #Break and return from function just below target altitude.
            if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
                print("Reached target altitude")
                break
            time.sleep(1)
    
    def dkTakeOff(self):
        self.arm_and_takeoff(int(self.Altitude_Textbox.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FatqatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FatqatMainWindow()
    ui.setupUi(FatqatMainWindow)
    FatqatMainWindow.show()
    sys.exit(app.exec_())

