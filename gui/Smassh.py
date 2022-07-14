# Form implementation generated from reading ui file '.\smassh.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_wdg_smash(object):
    def setupUi(self, wdg_smash):
        wdg_smash.setObjectName("wdg_smash")
        wdg_smash.resize(1254, 735)
        self.gridLayout = QtWidgets.QGridLayout(wdg_smash)
        self.gridLayout.setObjectName("gridLayout")
        self.frm_right = QtWidgets.QFrame(wdg_smash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_right.sizePolicy().hasHeightForWidth())
        self.frm_right.setSizePolicy(sizePolicy)
        self.frm_right.setMinimumSize(QtCore.QSize(79, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frm_right.setFont(font)
        self.frm_right.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_right.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frm_right.setLineWidth(0)
        self.frm_right.setObjectName("frm_right")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frm_right)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add_node = QtWidgets.QPushButton(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add_node.setFont(font)
        self.btn_add_node.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_add_node.setFlat(True)
        self.btn_add_node.setObjectName("btn_add_node")
        self.verticalLayout.addWidget(self.btn_add_node)
        self.btn_remove_node = QtWidgets.QPushButton(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_remove_node.setFont(font)
        self.btn_remove_node.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_remove_node.setFlat(True)
        self.btn_remove_node.setObjectName("btn_remove_node")
        self.verticalLayout.addWidget(self.btn_remove_node)
        self.btn_load_file = QtWidgets.QPushButton(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_load_file.setFont(font)
        self.btn_load_file.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_load_file.setFlat(True)
        self.btn_load_file.setObjectName("btn_load_file")
        self.verticalLayout.addWidget(self.btn_load_file)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frm_right)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spn_port = QtWidgets.QSpinBox(self.frm_right)
        self.spn_port.setMinimum(0)
        self.spn_port.setMaximum(65535)
        self.spn_port.setProperty("value", 22)
        self.spn_port.setObjectName("spn_port")
        self.verticalLayout.addWidget(self.spn_port)
        self.lbl_wait_buffer = QtWidgets.QLabel(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_wait_buffer.setFont(font)
        self.lbl_wait_buffer.setObjectName("lbl_wait_buffer")
        self.verticalLayout.addWidget(self.lbl_wait_buffer)
        self.spn_wait_buffer = QtWidgets.QDoubleSpinBox(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spn_wait_buffer.setFont(font)
        self.spn_wait_buffer.setMinimum(0.1)
        self.spn_wait_buffer.setMaximum(2.0)
        self.spn_wait_buffer.setSingleStep(0.1)
        self.spn_wait_buffer.setObjectName("spn_wait_buffer")
        self.verticalLayout.addWidget(self.spn_wait_buffer)
        self.lbl_timeout = QtWidgets.QLabel(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_timeout.setFont(font)
        self.lbl_timeout.setObjectName("lbl_timeout")
        self.verticalLayout.addWidget(self.lbl_timeout)
        self.spn_timeout = QtWidgets.QSpinBox(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spn_timeout.setFont(font)
        self.spn_timeout.setMinimum(1)
        self.spn_timeout.setMaximum(60)
        self.spn_timeout.setProperty("value", 10)
        self.spn_timeout.setObjectName("spn_timeout")
        self.verticalLayout.addWidget(self.spn_timeout)
        self.lbl_threads = QtWidgets.QLabel(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_threads.setFont(font)
        self.lbl_threads.setObjectName("lbl_threads")
        self.verticalLayout.addWidget(self.lbl_threads)
        self.spn_threads = QtWidgets.QSpinBox(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spn_threads.setFont(font)
        self.spn_threads.setMinimum(1)
        self.spn_threads.setMaximum(1000)
        self.spn_threads.setSingleStep(1)
        self.spn_threads.setProperty("value", 2)
        self.spn_threads.setObjectName("spn_threads")
        self.verticalLayout.addWidget(self.spn_threads)
        self.btn_smash = QtWidgets.QPushButton(self.frm_right)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_smash.setFont(font)
        self.btn_smash.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_smash.setFlat(True)
        self.btn_smash.setObjectName("btn_smash")
        self.verticalLayout.addWidget(self.btn_smash)
        self.gridLayout.addWidget(self.frm_right, 1, 3, 1, 1)
        self.lbl_nodes_try = QtWidgets.QLabel(wdg_smash)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_nodes_try.setFont(font)
        self.lbl_nodes_try.setObjectName("lbl_nodes_try")
        self.gridLayout.addWidget(self.lbl_nodes_try, 0, 2, 1, 1)
        self.tbl_smash_view = QtWidgets.QTableView(wdg_smash)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tbl_smash_view.setFont(font)
        self.tbl_smash_view.setAutoFillBackground(False)
        self.tbl_smash_view.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tbl_smash_view.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.tbl_smash_view.setObjectName("tbl_smash_view")
        self.gridLayout.addWidget(self.tbl_smash_view, 1, 2, 1, 1)
        self.btn_save_results = QtWidgets.QPushButton(wdg_smash)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save_results.setFont(font)
        self.btn_save_results.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_save_results.setFlat(True)
        self.btn_save_results.setObjectName("btn_save_results")
        self.gridLayout.addWidget(self.btn_save_results, 2, 2, 1, 1)
        self.frm_left = QtWidgets.QFrame(wdg_smash)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frm_left.setFont(font)
        self.frm_left.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_left.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frm_left.setLineWidth(0)
        self.frm_left.setObjectName("frm_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_left)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_duplicate_line = QtWidgets.QPushButton(self.frm_left)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_duplicate_line.setFont(font)
        self.btn_duplicate_line.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_duplicate_line.setFlat(True)
        self.btn_duplicate_line.setObjectName("btn_duplicate_line")
        self.verticalLayout_2.addWidget(self.btn_duplicate_line)
        self.btn_ip_range = QtWidgets.QPushButton(self.frm_left)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ip_range.setFont(font)
        self.btn_ip_range.setStyleSheet("QPushButton{\n"
"    color: rgb(250, 250, 250);\n"
"    background-color: rgb(0, 182, 48);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 135, 34);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 48, 12);\n"
"}")
        self.btn_ip_range.setObjectName("btn_ip_range")
        self.verticalLayout_2.addWidget(self.btn_ip_range)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frm_left, 1, 0, 1, 1)

        self.retranslateUi(wdg_smash)
        QtCore.QMetaObject.connectSlotsByName(wdg_smash)

    def retranslateUi(self, wdg_smash):
        _translate = QtCore.QCoreApplication.translate
        wdg_smash.setWindowTitle(_translate("wdg_smash", "Form"))
        self.btn_add_node.setText(_translate("wdg_smash", "Add Node"))
        self.btn_remove_node.setText(_translate("wdg_smash", "Remove Node"))
        self.btn_load_file.setText(_translate("wdg_smash", "Load file..."))
        self.label.setText(_translate("wdg_smash", "Port"))
        self.lbl_wait_buffer.setText(_translate("wdg_smash", "Wait for Buffer"))
        self.lbl_timeout.setText(_translate("wdg_smash", "Conn Timeout"))
        self.lbl_threads.setText(_translate("wdg_smash", "Threads"))
        self.btn_smash.setText(_translate("wdg_smash", "SMASH"))
        self.lbl_nodes_try.setText(_translate("wdg_smash", "Nodes to try:"))
        self.btn_save_results.setText(_translate("wdg_smash", "Save Results..."))
        self.btn_duplicate_line.setText(_translate("wdg_smash", "Duplicate\n"
" selected lines"))
        self.btn_ip_range.setText(_translate("wdg_smash", "IP Range \n"
" Command"))