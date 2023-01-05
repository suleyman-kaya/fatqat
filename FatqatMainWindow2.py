# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FatqatMainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import socket, time, os
from dronekit import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FatqatMainWindow(object):
    def setupUi(self, FatqatMainWindow):
        FatqatMainWindow.setObjectName("FatqatMainWindow")
        FatqatMainWindow.resize(561, 560)
        self.centralwidget = QtWidgets.QWidget(FatqatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConnectionString_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ConnectionString_Textbox.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.ConnectionString_Textbox.setObjectName("ConnectionString_Textbox")
        self.Btn_Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Connect.setGeometry(QtCore.QRect(180, 10, 89, 25))
        self.Btn_Connect.setObjectName("Btn_Connect")
        self.VehicleStateTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.VehicleStateTextbox.setGeometry(QtCore.QRect(10, 90, 261, 411))
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
        self.line.setGeometry(QtCore.QRect(10, 60, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Altitude_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Altitude_Textbox.setGeometry(QtCore.QRect(360, 10, 111, 25))
        self.Altitude_Textbox.setObjectName("Altitude_Textbox")
        self.AltitudeLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeLabel.setGeometry(QtCore.QRect(290, 12, 67, 20))
        self.AltitudeLabel.setObjectName("AltitudeLabel")
        self.TakeOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.TakeOffButton.setGeometry(QtCore.QRect(480, 10, 71, 25))
        self.TakeOffButton.setObjectName("TakeOffButton")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(280, 60, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.LocationTextbox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LocationTextbox1.setGeometry(QtCore.QRect(290, 90, 101, 25))
        self.LocationTextbox1.setObjectName("LocationTextbox1")
        self.GotoThisLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.GotoThisLocationButton.setGeometry(QtCore.QRect(290, 120, 261, 25))
        self.GotoThisLocationButton.setObjectName("GotoThisLocationButton")
        self.LocationTextbox2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LocationTextbox2.setGeometry(QtCore.QRect(400, 90, 101, 25))
        self.LocationTextbox2.setObjectName("LocationTextbox2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(290, 170, 261, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(263, 10, 31, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.AltitudeStatusTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeStatusTextLabel.setGeometry(QtCore.QRect(290, 40, 111, 17))
        self.AltitudeStatusTextLabel.setObjectName("AltitudeStatusTextLabel")
        self.AltitudeStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeStatusLabel.setGeometry(QtCore.QRect(400, 40, 151, 17))
        self.AltitudeStatusLabel.setObjectName("AltitudeStatusLabel")
        self.simpleGotoTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.simpleGotoTextLabel.setGeometry(QtCore.QRect(290, 150, 111, 17))
        self.simpleGotoTextLabel.setObjectName("simpleGotoTextLabel")
        self.simpleGotoStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.simpleGotoStatusLabel.setGeometry(QtCore.QRect(340, 150, 151, 17))
        self.simpleGotoStatusLabel.setObjectName("simpleGotoStatusLabel")
        self.airspeedTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.airspeedTextbox.setGeometry(QtCore.QRect(450, 190, 51, 25))
        self.airspeedTextbox.setObjectName("airspeedTextbox")
        self.airspeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.airspeedLabel.setGeometry(QtCore.QRect(290, 192, 161, 21))
        self.airspeedLabel.setObjectName("airspeedLabel")
        self.setAirSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.setAirSpeedButton.setGeometry(QtCore.QRect(510, 190, 41, 25))
        self.setAirSpeedButton.setObjectName("setAirSpeedButton")
        self.groundSpeedTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.groundSpeedTextbox.setGeometry(QtCore.QRect(450, 220, 51, 25))
        self.groundSpeedTextbox.setObjectName("groundSpeedTextbox")
        self.groundSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.groundSpeedLabel.setGeometry(QtCore.QRect(290, 222, 161, 21))
        self.groundSpeedLabel.setObjectName("groundSpeedLabel")
        self.setGroundSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.setGroundSpeedButton.setGeometry(QtCore.QRect(510, 220, 41, 25))
        self.setGroundSpeedButton.setObjectName("setGroundSpeedButton")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(290, 250, 261, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.durationTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.durationTextbox.setGeometry(QtCore.QRect(500, 270, 51, 25))
        self.durationTextbox.setObjectName("durationTextbox")
        self.xVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.xVelocityTextbox.setGeometry(QtCore.QRect(290, 270, 61, 25))
        self.xVelocityTextbox.setObjectName("xVelocityTextbox")
        self.yVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.yVelocityTextbox.setGeometry(QtCore.QRect(360, 270, 61, 25))
        self.yVelocityTextbox.setObjectName("yVelocityTextbox")
        self.zVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.zVelocityTextbox.setGeometry(QtCore.QRect(430, 270, 61, 25))
        self.zVelocityTextbox.setObjectName("zVelocityTextbox")
        self.sendNedVelocityButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendNedVelocityButton.setGeometry(QtCore.QRect(290, 300, 261, 25))
        self.sendNedVelocityButton.setObjectName("sendNedVelocityButton")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(290, 330, 261, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.SetVehicleModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.SetVehicleModeLabel.setGeometry(QtCore.QRect(290, 350, 131, 17))
        self.SetVehicleModeLabel.setObjectName("SetVehicleModeLabel")
        self.SetVehicleModeStabilizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeStabilizeButton.setGeometry(QtCore.QRect(290, 370, 89, 25))
        self.SetVehicleModeStabilizeButton.setObjectName("SetVehicleModeStabilizeButton")
        self.SetVehicleModeGuidedButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeGuidedButton.setGeometry(QtCore.QRect(390, 370, 89, 25))
        self.SetVehicleModeGuidedButton.setObjectName("SetVehicleModeGuidedButton")
        self.SetVehicleModeRTLButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeRTLButton.setGeometry(QtCore.QRect(490, 370, 61, 25))
        self.SetVehicleModeRTLButton.setObjectName("SetVehicleModeRTLButton")
        self.SetVehicleModeLandButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeLandButton.setGeometry(QtCore.QRect(430, 400, 121, 25))
        self.SetVehicleModeLandButton.setObjectName("SetVehicleModeLandButton")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(290, 430, 261, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.ControllingWithKeysButton = QtWidgets.QPushButton(self.centralwidget)
        self.ControllingWithKeysButton.setGeometry(QtCore.QRect(290, 480, 261, 25))
        self.ControllingWithKeysButton.setObjectName("ControllingWithKeysButton")
        self.AltTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.AltTextbox.setGeometry(QtCore.QRect(510, 90, 41, 25))
        self.AltTextbox.setObjectName("AltTextbox")
        self.ArrowsControlConnectionStringTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ArrowsControlConnectionStringTextbox.setGeometry(QtCore.QRect(420, 450, 131, 25))
        self.ArrowsControlConnectionStringTextbox.setObjectName("ArrowsControlConnectionStringTextbox")
        self.arrowsControlLabel = QtWidgets.QLabel(self.centralwidget)
        self.arrowsControlLabel.setGeometry(QtCore.QRect(290, 450, 131, 20))
        self.arrowsControlLabel.setObjectName("arrowsControlLabel")
        self.SetVehicleModeAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeAutoButton.setGeometry(QtCore.QRect(290, 400, 121, 25))
        self.SetVehicleModeAutoButton.setObjectName("SetVehicleModeAutoButton")
        FatqatMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FatqatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 22))
        self.menubar.setObjectName("menubar")
        FatqatMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FatqatMainWindow)
        self.statusbar.setObjectName("statusbar")
        FatqatMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FatqatMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FatqatMainWindow)

        self.Btn_Connect.clicked.connect(self.dkConnect)
        self.TakeOffButton.clicked.connect(self.dkTakeOff)
        self.GotoThisLocationButton.clicked.connect(self.dkSimpleGoto)
        self.setAirSpeedButton.clicked.connect(self.dkSetVehicleAirspeed)
        self.setGroundSpeedButton.clicked.connect(self.dkSetVehicleGroundspeed)
        self.sendNedVelocityButton.clicked.connect(self.dkSendNedVelocity)
        self.SetVehicleModeStabilizeButton.clicked.connect(self.dkSetVehicleModeStabilize)
        self.SetVehicleModeGuidedButton.clicked.connect(self.dkSetVehicleModeGuided)
        self.SetVehicleModeRTLButton.clicked.connect(self.dkSetVehicleModeRTL)
        self.SetVehicleModeLandButton.clicked.connect(self.dkSetVehicleModeLand)
        self.SetVehicleModeAutoButton.clicked.connect(self.dkSetVehicleModeAuto)
        self.ControllingWithKeysButton.clicked.connect(self.dkArrowKeysControl)

    def retranslateUi(self, FatqatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FatqatMainWindow.setWindowTitle(_translate("FatqatMainWindow", "Fatqat - Ground Control Station Software"))
        self.Btn_Connect.setText(_translate("FatqatMainWindow", "Connect!"))
        self.ConnectionStatusTextLabel.setText(_translate("FatqatMainWindow", "Connection Status:"))
        self.ConnectionStatusLabel.setText(_translate("FatqatMainWindow", "Not Connected"))
        self.VehicleStateLabel.setText(_translate("FatqatMainWindow", "Vehicle State:"))
        self.AltitudeLabel.setText(_translate("FatqatMainWindow", "Altitude:"))
        self.TakeOffButton.setText(_translate("FatqatMainWindow", "Take-off!"))
        self.LocationTextbox1.setText(_translate("FatqatMainWindow", "Latitude"))
        self.GotoThisLocationButton.setText(_translate("FatqatMainWindow", "Go to this location!"))
        self.LocationTextbox2.setText(_translate("FatqatMainWindow", "Longtitude"))
        self.AltitudeStatusTextLabel.setText(_translate("FatqatMainWindow", "Takeoff Status:"))
        self.AltitudeStatusLabel.setText(_translate("FatqatMainWindow", "Not reached target alt"))
        self.simpleGotoTextLabel.setText(_translate("FatqatMainWindow", "Status:"))
        self.simpleGotoStatusLabel.setText(_translate("FatqatMainWindow", "Undone"))
        self.airspeedLabel.setText(_translate("FatqatMainWindow", "Vehicle Airspeed (m/s):"))
        self.setAirSpeedButton.setText(_translate("FatqatMainWindow", "Set"))
        self.groundSpeedLabel.setText(_translate("FatqatMainWindow", "Ground speed (m/s):"))
        self.setGroundSpeedButton.setText(_translate("FatqatMainWindow", "Set"))
        self.sendNedVelocityButton.setText(_translate("FatqatMainWindow", "send_ned_velocity(x, y, z, duration)"))
        self.SetVehicleModeLabel.setText(_translate("FatqatMainWindow", "Set Vehicle Mode:"))
        self.SetVehicleModeStabilizeButton.setText(_translate("FatqatMainWindow", "STABILIZE"))
        self.SetVehicleModeGuidedButton.setText(_translate("FatqatMainWindow", "GUIDED"))
        self.SetVehicleModeRTLButton.setText(_translate("FatqatMainWindow", "RTL"))
        self.SetVehicleModeLandButton.setText(_translate("FatqatMainWindow", "LAND"))
        self.ControllingWithKeysButton.setText(_translate("FatqatMainWindow", "Control Vehicle With Arrow Keys"))
        self.AltTextbox.setText(_translate("FatqatMainWindow", "Alt"))
        self.arrowsControlLabel.setText(_translate("FatqatMainWindow", "Connection String:"))
        self.SetVehicleModeAutoButton.setText(_translate("FatqatMainWindow", "AUTO"))

    def dkConnect(self):
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
            connectionStatus = "UDP Connection or Some other error!"
            self.ConnectionStatusLabel.setText(connectionStatus)
            self.dkGetVehicleState()

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
                self.AltitudeStatusLabel.setText("Reached target altitude")
                break
            time.sleep(1)
    
    def dkTakeOff(self):
        self.arm_and_takeoff(int(self.Altitude_Textbox.text()))

    def dkSimpleGoto(self):
        vehicle.mode = VehicleMode("GUIDED")
        a_location = LocationGlobalRelative(float(self.LocationTextbox1.text()), float(self.LocationTextbox2.text()), int(self.AltTextbox.text()))
        vehicle.simple_goto(a_location)
        self.simpleGotoStatusLabel.setText("Done.")

    def dkSetVehicleAirspeed(self):
        print("Undone:Airspeed:%s" % vehicle.airspeed)
        vehicle.airspeed = float(self.airspeedTextbox.text())
        print("Done:Airspeed:%s" % vehicle.airspeed)
    
    def dkSetVehicleGroundspeed(self):
        print("Undone:Groundspeed:%s" % vehicle.groundspeed)
        vehicle.groundspeed = float(self.groundSpeedTextbox.text())
        print("Done:Groundspeed:%s" % vehicle.groundspeed)

    def send_ned_velocity(self, velocity_x, velocity_y, velocity_z, duration):
        """
        Move vehicle in direction based on specified velocity vectors.
        """
        msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,       # time_boot_ms (not used)
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
            0b0000111111000111, # type_mask (only speeds enabled)
            0, 0, 0, # x, y, z positions (not used)
            velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
            0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


        # send command to vehicle on 1 Hz cycle
        for x in range(0,duration):
            vehicle.send_mavlink(msg)
            time.sleep(1)

    def dkSendNedVelocity(self):
        print("called function: send_ned_velocity()")
        self.send_ned_velocity(float(self.xVelocityTextbox.text()),float(self.yVelocityTextbox.text()),float(self.zVelocityTextbox.text()),int(self.durationTextbox.text()))
        print("called function returns value 0, so it worked!")

    def dkSetVehicleModeStabilize(self):
        print("Current vehicle mode: %s" % vehicle.mode)
        vehicle.mode = "STABILIZE"
        print("Updated vehicle mode: %s" % vehicle.mode)

    def dkSetVehicleModeGuided(self):
        print("Current vehicle mode: %s" % vehicle.mode)
        vehicle.mode = "GUIDED"
        print("Updated vehicle mode: %s" % vehicle.mode)

    def dkSetVehicleModeRTL(self):
        print("Current vehicle mode: %s" % vehicle.mode)
        vehicle.mode = "RTL"
        print("Updated vehicle mode: %s" % vehicle.mode)

    def dkSetVehicleModeLand(self):
        print("Current vehicle mode: %s" % vehicle.mode)
        vehicle.mode = "LAND"
        print("Updated vehicle mode: %s" % vehicle.mode)
    
    def dkSetVehicleModeAuto(self):
        print("Current vehicle mode: %s" % vehicle.mode)
        vehicle.mode = "AUTO"
        print("Updated vehicle mode: %s" % vehicle.mode)

    def dkArrowKeysControl(self):
        connectionStringForArrows = self.ArrowsControlConnectionStringTextbox.text()
        os.system("python3 arrowControls.py %s" % connectionStringForArrows)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FatqatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FatqatMainWindow()
    ui.setupUi(FatqatMainWindow)
    FatqatMainWindow.show()
    sys.exit(app.exec_())