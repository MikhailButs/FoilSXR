# Form implementation generated from reading ui file 'dataWindowUiDesign.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DataWidget(object):
    def setupUi(self, DataWidget):
        DataWidget.setObjectName("DataWidget")
        DataWidget.resize(1097, 838)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(DataWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=DataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.profile_verticalLayout = QtWidgets.QVBoxLayout()
        self.profile_verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.profile_verticalLayout.setObjectName("profile_verticalLayout")
        self.verticalLayout_4.addLayout(self.profile_verticalLayout)
        self.slider_horizontalLayout = QtWidgets.QHBoxLayout()
        self.slider_horizontalLayout.setObjectName("slider_horizontalLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.slider_horizontalLayout.addWidget(self.label_8)
        self.time_label = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setObjectName("time_label")
        self.slider_horizontalLayout.addWidget(self.time_label)
        self.time_horizontalSlider = QtWidgets.QSlider(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.time_horizontalSlider.setSizePolicy(sizePolicy)
        self.time_horizontalSlider.setMaximum(0)
        self.time_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.time_horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.time_horizontalSlider.setTickInterval(0)
        self.time_horizontalSlider.setObjectName("time_horizontalSlider")
        self.slider_horizontalLayout.addWidget(self.time_horizontalSlider)
        self.verticalLayout_4.addLayout(self.slider_horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.frame_3 = QtWidgets.QFrame(parent=DataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(240, 450))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calculate_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.verticalLayout.addWidget(self.calculate_pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.foil1_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foil1_comboBox.sizePolicy().hasHeightForWidth())
        self.foil1_comboBox.setSizePolicy(sizePolicy)
        self.foil1_comboBox.setObjectName("foil1_comboBox")
        self.foil1_comboBox.addItem("")
        self.foil1_comboBox.addItem("")
        self.foil1_comboBox.addItem("")
        self.foil1_comboBox.addItem("")
        self.foil1_comboBox.addItem("")
        self.foil1_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.foil1_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.foil2_comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.foil2_comboBox.setObjectName("foil2_comboBox")
        self.foil2_comboBox.addItem("")
        self.foil2_comboBox.addItem("")
        self.foil2_comboBox.addItem("")
        self.foil2_comboBox.addItem("")
        self.foil2_comboBox.addItem("")
        self.foil2_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.foil2_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lowTime_spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.lowTime_spinBox.setProperty("value", 1)
        self.lowTime_spinBox.setObjectName("lowTime_spinBox")
        self.horizontalLayout_4.addWidget(self.lowTime_spinBox)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.highTime_spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.highTime_spinBox.setProperty("value", 10)
        self.highTime_spinBox.setObjectName("highTime_spinBox")
        self.horizontalLayout_4.addWidget(self.highTime_spinBox)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.threshold_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.groupBox)
        self.threshold_doubleSpinBox.setDecimals(1)
        self.threshold_doubleSpinBox.setSingleStep(0.1)
        self.threshold_doubleSpinBox.setProperty("value", 2.0)
        self.threshold_doubleSpinBox.setObjectName("threshold_doubleSpinBox")
        self.horizontalLayout_5.addWidget(self.threshold_doubleSpinBox)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.smoothing_spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.smoothing_spinBox.setMaximum(999)
        self.smoothing_spinBox.setProperty("value", 50)
        self.smoothing_spinBox.setObjectName("smoothing_spinBox")
        self.horizontalLayout_3.addWidget(self.smoothing_spinBox)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(parent=self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.show1_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show1_checkBox.setObjectName("show1_checkBox")
        self.verticalLayout.addWidget(self.show1_checkBox)
        self.show2_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show2_checkBox.setObjectName("show2_checkBox")
        self.verticalLayout.addWidget(self.show2_checkBox)
        self.show3_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show3_checkBox.setObjectName("show3_checkBox")
        self.verticalLayout.addWidget(self.show3_checkBox)
        self.show4_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show4_checkBox.setObjectName("show4_checkBox")
        self.verticalLayout.addWidget(self.show4_checkBox)
        self.show5_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show5_checkBox.setObjectName("show5_checkBox")
        self.verticalLayout.addWidget(self.show5_checkBox)
        self.show6_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show6_checkBox.setObjectName("show6_checkBox")
        self.verticalLayout.addWidget(self.show6_checkBox)
        self.show7_checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.show7_checkBox.setObjectName("show7_checkBox")
        self.verticalLayout.addWidget(self.show7_checkBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.frame = QtWidgets.QFrame(parent=DataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.timeTrace_verticalLayout = QtWidgets.QVBoxLayout()
        self.timeTrace_verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.timeTrace_verticalLayout.setObjectName("timeTrace_verticalLayout")
        self.verticalLayout_3.addLayout(self.timeTrace_verticalLayout)
        self.verticalLayout_6.addWidget(self.frame)

        self.retranslateUi(DataWidget)
        QtCore.QMetaObject.connectSlotsByName(DataWidget)

    def retranslateUi(self, DataWidget):
        _translate = QtCore.QCoreApplication.translate
        DataWidget.setWindowTitle(_translate("DataWidget", "Data processing"))
        self.label_8.setText(_translate("DataWidget", "Current time:"))
        self.time_label.setText(_translate("DataWidget", "0"))
        self.groupBox.setTitle(_translate("DataWidget", "Signals managing"))
        self.calculate_pushButton.setText(_translate("DataWidget", "CALCULATE"))
        self.label.setText(_translate("DataWidget", "Foil 1:"))
        self.foil1_comboBox.setItemText(0, _translate("DataWidget", "100"))
        self.foil1_comboBox.setItemText(1, _translate("DataWidget", "200"))
        self.foil1_comboBox.setItemText(2, _translate("DataWidget", "300"))
        self.foil1_comboBox.setItemText(3, _translate("DataWidget", "400"))
        self.foil1_comboBox.setItemText(4, _translate("DataWidget", "500"))
        self.foil1_comboBox.setItemText(5, _translate("DataWidget", "700"))
        self.label_2.setText(_translate("DataWidget", "Foil 2:"))
        self.foil2_comboBox.setItemText(0, _translate("DataWidget", "100"))
        self.foil2_comboBox.setItemText(1, _translate("DataWidget", "200"))
        self.foil2_comboBox.setItemText(2, _translate("DataWidget", "300"))
        self.foil2_comboBox.setItemText(3, _translate("DataWidget", "400"))
        self.foil2_comboBox.setItemText(4, _translate("DataWidget", "500"))
        self.foil2_comboBox.setItemText(5, _translate("DataWidget", "700"))
        self.label_3.setText(_translate("DataWidget", "Signal-free time"))
        self.label_4.setText(_translate("DataWidget", "-"))
        self.label_5.setText(_translate("DataWidget", "ms"))
        self.label_6.setText(_translate("DataWidget", "Noise threshold"))
        self.label_7.setText(_translate("DataWidget", "sigma"))
        self.label_9.setText(_translate("DataWidget", "Smoothing"))
        self.label_10.setText(_translate("DataWidget", "points"))
        self.label_11.setText(_translate("DataWidget", "Temperatures to plot"))
        self.show1_checkBox.setText(_translate("DataWidget", "T 1-2"))
        self.show2_checkBox.setText(_translate("DataWidget", "T 3-4"))
        self.show3_checkBox.setText(_translate("DataWidget", "T 5-6"))
        self.show4_checkBox.setText(_translate("DataWidget", "T 7-8"))
        self.show5_checkBox.setText(_translate("DataWidget", "T 8-9"))
        self.show6_checkBox.setText(_translate("DataWidget", "T 9-10"))
        self.show7_checkBox.setText(_translate("DataWidget", "T 11-12"))
