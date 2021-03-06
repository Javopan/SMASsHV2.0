# Form implementation generated from reading ui file '.\iprange-dialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon.fromTheme("Fusion")
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 20px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_ip_end = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_ip_end.setFont(font)
        self.lbl_ip_end.setObjectName("lbl_ip_end")
        self.gridLayout.addWidget(self.lbl_ip_end, 1, 0, 1, 1)
        self.btn_box = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_box.setFont(font)
        self.btn_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btn_box.setObjectName("btn_box")
        self.gridLayout.addWidget(self.btn_box, 6, 0, 1, 2)
        self.txt_reps = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_reps.setFont(font)
        self.txt_reps.setObjectName("txt_reps")
        self.gridLayout.addWidget(self.txt_reps, 2, 1, 1, 1)
        self.lbl_ip_start = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_ip_start.setFont(font)
        self.lbl_ip_start.setObjectName("lbl_ip_start")
        self.gridLayout.addWidget(self.lbl_ip_start, 0, 0, 1, 1)
        self.txt_ip_end = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_ip_end.setFont(font)
        self.txt_ip_end.setText("")
        self.txt_ip_end.setObjectName("txt_ip_end")
        self.gridLayout.addWidget(self.txt_ip_end, 1, 1, 1, 1)
        self.txt_ip_start = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_ip_start.setFont(font)
        self.txt_ip_start.setObjectName("txt_ip_start")
        self.gridLayout.addWidget(self.txt_ip_start, 0, 1, 1, 1)
        self.lbl_repetitions = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_repetitions.setFont(font)
        self.lbl_repetitions.setObjectName("lbl_repetitions")
        self.gridLayout.addWidget(self.lbl_repetitions, 2, 0, 1, 1)
        self.lbl_commands = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_commands.setFont(font)
        self.lbl_commands.setObjectName("lbl_commands")
        self.gridLayout.addWidget(self.lbl_commands, 3, 0, 1, 1)
        self.txt_commands = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_commands.setFont(font)
        self.txt_commands.setObjectName("txt_commands")
        self.gridLayout.addWidget(self.txt_commands, 3, 1, 1, 1)
        self.lbl_username = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.gridLayout.addWidget(self.lbl_username, 4, 0, 1, 1)
        self.lbl_pass = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_pass.setFont(font)
        self.lbl_pass.setObjectName("lbl_pass")
        self.gridLayout.addWidget(self.lbl_pass, 5, 0, 1, 1)
        self.txt_user = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_user.setFont(font)
        self.txt_user.setObjectName("txt_user")
        self.gridLayout.addWidget(self.txt_user, 4, 1, 1, 1)
        self.txt_pass = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_pass.setFont(font)
        self.txt_pass.setObjectName("txt_pass")
        self.gridLayout.addWidget(self.txt_pass, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.btn_box.accepted.connect(Dialog.accept) # type: ignore
        self.btn_box.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txt_ip_start, self.txt_ip_end)
        Dialog.setTabOrder(self.txt_ip_end, self.txt_reps)
        Dialog.setTabOrder(self.txt_reps, self.txt_commands)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_ip_end.setText(_translate("Dialog", "IP END"))
        self.txt_reps.setPlaceholderText(_translate("Dialog", "repetitions"))
        self.lbl_ip_start.setText(_translate("Dialog", "IP Start"))
        self.txt_ip_end.setPlaceholderText(_translate("Dialog", "IP to end"))
        self.txt_ip_start.setPlaceholderText(_translate("Dialog", "IP to start"))
        self.lbl_repetitions.setText(_translate("Dialog", "Repetitions"))
        self.lbl_commands.setText(_translate("Dialog", "Commands"))
        self.txt_commands.setPlaceholderText(_translate("Dialog", "Commands"))
        self.lbl_username.setText(_translate("Dialog", "Username"))
        self.lbl_pass.setText(_translate("Dialog", "Password"))
        self.txt_user.setPlaceholderText(_translate("Dialog", "Username"))
        self.txt_pass.setPlaceholderText(_translate("Dialog", "Password"))
