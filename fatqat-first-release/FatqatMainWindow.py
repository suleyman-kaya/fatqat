# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FatqatMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FatqatMainWindow(object):
    def setupUi(self, FatqatMainWindow):
        FatqatMainWindow.setObjectName("FatqatMainWindow")
        FatqatMainWindow.resize(1424, 567)
        self.centralwidget = QtWidgets.QWidget(FatqatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConnectionString_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ConnectionString_Textbox.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.ConnectionString_Textbox.setObjectName("ConnectionString_Textbox")
        self.Btn_Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Connect.setGeometry(QtCore.QRect(180, 10, 89, 25))
        self.Btn_Connect.setObjectName("Btn_Connect")
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
        self.line.setGeometry(QtCore.QRect(10, 60, 475, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Altitude_Textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Altitude_Textbox.setGeometry(QtCore.QRect(560, 10, 111, 25))
        self.Altitude_Textbox.setObjectName("Altitude_Textbox")
        self.AltitudeLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeLabel.setGeometry(QtCore.QRect(490, 12, 67, 20))
        self.AltitudeLabel.setObjectName("AltitudeLabel")
        self.TakeOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.TakeOffButton.setGeometry(QtCore.QRect(680, 10, 71, 25))
        self.TakeOffButton.setObjectName("TakeOffButton")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(485, 60, 270, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.LocationTextbox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LocationTextbox1.setGeometry(QtCore.QRect(490, 90, 101, 25))
        self.LocationTextbox1.setObjectName("LocationTextbox1")
        self.GotoThisLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.GotoThisLocationButton.setGeometry(QtCore.QRect(490, 120, 261, 25))
        self.GotoThisLocationButton.setObjectName("GotoThisLocationButton")
        self.LocationTextbox2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LocationTextbox2.setGeometry(QtCore.QRect(600, 90, 101, 25))
        self.LocationTextbox2.setObjectName("LocationTextbox2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(490, 170, 261, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.AltitudeStatusTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeStatusTextLabel.setGeometry(QtCore.QRect(490, 40, 111, 17))
        self.AltitudeStatusTextLabel.setObjectName("AltitudeStatusTextLabel")
        self.AltitudeStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.AltitudeStatusLabel.setGeometry(QtCore.QRect(600, 40, 151, 17))
        self.AltitudeStatusLabel.setObjectName("AltitudeStatusLabel")
        self.simpleGotoTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.simpleGotoTextLabel.setGeometry(QtCore.QRect(490, 150, 111, 17))
        self.simpleGotoTextLabel.setObjectName("simpleGotoTextLabel")
        self.simpleGotoStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.simpleGotoStatusLabel.setGeometry(QtCore.QRect(540, 150, 151, 17))
        self.simpleGotoStatusLabel.setObjectName("simpleGotoStatusLabel")
        self.airspeedTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.airspeedTextbox.setGeometry(QtCore.QRect(650, 190, 51, 25))
        self.airspeedTextbox.setObjectName("airspeedTextbox")
        self.airspeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.airspeedLabel.setGeometry(QtCore.QRect(490, 192, 161, 21))
        self.airspeedLabel.setObjectName("airspeedLabel")
        self.setAirSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.setAirSpeedButton.setGeometry(QtCore.QRect(710, 190, 41, 25))
        self.setAirSpeedButton.setObjectName("setAirSpeedButton")
        self.groundSpeedTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.groundSpeedTextbox.setGeometry(QtCore.QRect(650, 220, 51, 25))
        self.groundSpeedTextbox.setObjectName("groundSpeedTextbox")
        self.groundSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.groundSpeedLabel.setGeometry(QtCore.QRect(490, 222, 161, 21))
        self.groundSpeedLabel.setObjectName("groundSpeedLabel")
        self.setGroundSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.setGroundSpeedButton.setGeometry(QtCore.QRect(710, 220, 41, 25))
        self.setGroundSpeedButton.setObjectName("setGroundSpeedButton")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(490, 250, 261, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.durationTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.durationTextbox.setGeometry(QtCore.QRect(700, 270, 51, 25))
        self.durationTextbox.setObjectName("durationTextbox")
        self.xVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.xVelocityTextbox.setGeometry(QtCore.QRect(490, 270, 61, 25))
        self.xVelocityTextbox.setObjectName("xVelocityTextbox")
        self.yVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.yVelocityTextbox.setGeometry(QtCore.QRect(560, 270, 61, 25))
        self.yVelocityTextbox.setObjectName("yVelocityTextbox")
        self.zVelocityTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.zVelocityTextbox.setGeometry(QtCore.QRect(630, 270, 61, 25))
        self.zVelocityTextbox.setObjectName("zVelocityTextbox")
        self.sendNedVelocityButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendNedVelocityButton.setGeometry(QtCore.QRect(490, 300, 261, 25))
        self.sendNedVelocityButton.setObjectName("sendNedVelocityButton")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(490, 330, 261, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.SetVehicleModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.SetVehicleModeLabel.setGeometry(QtCore.QRect(490, 350, 131, 17))
        self.SetVehicleModeLabel.setObjectName("SetVehicleModeLabel")
        self.SetVehicleModeStabilizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeStabilizeButton.setGeometry(QtCore.QRect(490, 370, 89, 25))
        self.SetVehicleModeStabilizeButton.setObjectName("SetVehicleModeStabilizeButton")
        self.SetVehicleModeGuidedButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeGuidedButton.setGeometry(QtCore.QRect(590, 370, 89, 25))
        self.SetVehicleModeGuidedButton.setObjectName("SetVehicleModeGuidedButton")
        self.SetVehicleModeRTLButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeRTLButton.setGeometry(QtCore.QRect(690, 370, 61, 25))
        self.SetVehicleModeRTLButton.setObjectName("SetVehicleModeRTLButton")
        self.SetVehicleModeLandButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeLandButton.setGeometry(QtCore.QRect(630, 400, 121, 25))
        self.SetVehicleModeLandButton.setObjectName("SetVehicleModeLandButton")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(490, 430, 261, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.ControllingWithKeysButton = QtWidgets.QPushButton(self.centralwidget)
        self.ControllingWithKeysButton.setGeometry(QtCore.QRect(490, 480, 261, 25))
        self.ControllingWithKeysButton.setObjectName("ControllingWithKeysButton")
        self.AltTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.AltTextbox.setGeometry(QtCore.QRect(710, 90, 41, 25))
        self.AltTextbox.setObjectName("AltTextbox")
        self.ArrowsControlConnectionStringTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ArrowsControlConnectionStringTextbox.setGeometry(QtCore.QRect(620, 450, 131, 25))
        self.ArrowsControlConnectionStringTextbox.setObjectName("ArrowsControlConnectionStringTextbox")
        self.arrowsControlLabel = QtWidgets.QLabel(self.centralwidget)
        self.arrowsControlLabel.setGeometry(QtCore.QRect(490, 450, 131, 20))
        self.arrowsControlLabel.setObjectName("arrowsControlLabel")
        self.SetVehicleModeAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetVehicleModeAutoButton.setGeometry(QtCore.QRect(490, 400, 121, 25))
        self.SetVehicleModeAutoButton.setObjectName("SetVehicleModeAutoButton")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(754, 60, 668, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.ImportMissionButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportMissionButton.setGeometry(QtCore.QRect(760, 10, 141, 25))
        self.ImportMissionButton.setObjectName("ImportMissionButton")
        self.ExportCurrentMission = QtWidgets.QPushButton(self.centralwidget)
        self.ExportCurrentMission.setGeometry(QtCore.QRect(760, 40, 141, 25))
        self.ExportCurrentMission.setObjectName("ExportCurrentMission")
        self.ImportedFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImportedFileLabel.setGeometry(QtCore.QRect(910, 10, 91, 21))
        self.ImportedFileLabel.setObjectName("ImportedFileLabel")
        self.ExportedFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExportedFileLabel.setGeometry(QtCore.QRect(910, 40, 91, 21))
        self.ExportedFileLabel.setObjectName("ExportedFileLabel")
        self.VideoFeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoFeedLabel.setGeometry(QtCore.QRect(770, 80, 641, 421))
        self.VideoFeedLabel.setText("")
        self.VideoFeedLabel.setPixmap(QtGui.QPixmap("../Images/640x480.jpg"))
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(10, 0, 1410, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(485, 510, 935, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(470, 8, 31, 510))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(740, 7, 31, 510))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1010, 7, 3, 60))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.VehicleStateTextbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.VehicleStateTextbox.setGeometry(QtCore.QRect(10, 90, 471, 431))
        self.VehicleStateTextbox.setObjectName("VehicleStateTextbox")
        FatqatMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FatqatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1424, 18))
        self.menubar.setObjectName("menubar")
        FatqatMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FatqatMainWindow)
        self.statusbar.setObjectName("statusbar")
        FatqatMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FatqatMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FatqatMainWindow)

    def retranslateUi(self, FatqatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FatqatMainWindow.setWindowTitle(_translate("FatqatMainWindow", "Fatqat - Ground Control Station Software"))
        self.ConnectionString_Textbox.setText(_translate("FatqatMainWindow", "tcp:127.0.0.1:5762"))
        self.Btn_Connect.setText(_translate("FatqatMainWindow", "Connect!"))
        self.ConnectionStatusTextLabel.setText(_translate("FatqatMainWindow", "Connection Status:"))
        self.ConnectionStatusLabel.setText(_translate("FatqatMainWindow", "Not Connected"))
        self.VehicleStateLabel.setText(_translate("FatqatMainWindow", "Vehicle State:"))
        self.Altitude_Textbox.setText(_translate("FatqatMainWindow", "10"))
        self.AltitudeLabel.setText(_translate("FatqatMainWindow", "Altitude:"))
        self.TakeOffButton.setText(_translate("FatqatMainWindow", "Take-off!"))
        self.LocationTextbox1.setText(_translate("FatqatMainWindow", "Latitude"))
        self.GotoThisLocationButton.setText(_translate("FatqatMainWindow", "Go to this location!"))
        self.LocationTextbox2.setText(_translate("FatqatMainWindow", "Longtitude"))
        self.AltitudeStatusTextLabel.setText(_translate("FatqatMainWindow", "Takeoff Status:"))
        self.AltitudeStatusLabel.setText(_translate("FatqatMainWindow", "Not reached target alt"))
        self.simpleGotoTextLabel.setText(_translate("FatqatMainWindow", "Status:"))
        self.simpleGotoStatusLabel.setText(_translate("FatqatMainWindow", "Undone"))
        self.airspeedTextbox.setText(_translate("FatqatMainWindow", "101"))
        self.airspeedLabel.setText(_translate("FatqatMainWindow", "Vehicle Airspeed (m/s):"))
        self.setAirSpeedButton.setText(_translate("FatqatMainWindow", "Set"))
        self.groundSpeedTextbox.setText(_translate("FatqatMainWindow", "101"))
        self.groundSpeedLabel.setText(_translate("FatqatMainWindow", "Ground speed (m/s):"))
        self.setGroundSpeedButton.setText(_translate("FatqatMainWindow", "Set"))
        self.durationTextbox.setText(_translate("FatqatMainWindow", "time"))
        self.xVelocityTextbox.setText(_translate("FatqatMainWindow", "vel X"))
        self.yVelocityTextbox.setText(_translate("FatqatMainWindow", "vel Y"))
        self.zVelocityTextbox.setText(_translate("FatqatMainWindow", "vel Z"))
        self.sendNedVelocityButton.setText(_translate("FatqatMainWindow", "send_ned_velocity(x, y, z, duration)"))
        self.SetVehicleModeLabel.setText(_translate("FatqatMainWindow", "Set Vehicle Mode:"))
        self.SetVehicleModeStabilizeButton.setText(_translate("FatqatMainWindow", "STABILIZE"))
        self.SetVehicleModeGuidedButton.setText(_translate("FatqatMainWindow", "GUIDED"))
        self.SetVehicleModeRTLButton.setText(_translate("FatqatMainWindow", "RTL"))
        self.SetVehicleModeLandButton.setText(_translate("FatqatMainWindow", "LAND"))
        self.ControllingWithKeysButton.setText(_translate("FatqatMainWindow", "Control Vehicle With Arrow Keys"))
        self.AltTextbox.setText(_translate("FatqatMainWindow", "Alt"))
        self.ArrowsControlConnectionStringTextbox.setText(_translate("FatqatMainWindow", "udp:127.0.0.1:14551"))
        self.arrowsControlLabel.setText(_translate("FatqatMainWindow", "Connection String:"))
        self.SetVehicleModeAutoButton.setText(_translate("FatqatMainWindow", "AUTO"))
        self.ImportMissionButton.setText(_translate("FatqatMainWindow", "Import a Mission"))
        self.ExportCurrentMission.setText(_translate("FatqatMainWindow", "Export the Mission"))
        self.ImportedFileLabel.setText(_translate("FatqatMainWindow", "Imported file:"))
        self.ExportedFileLabel.setText(_translate("FatqatMainWindow", "Exported file:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FatqatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FatqatMainWindow()
    ui.setupUi(FatqatMainWindow)
    FatqatMainWindow.show()
    sys.exit(app.exec_())
