# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera-params-detached.ui'
#
# Created: Fri Jul 24 08:06:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(504, 95)
        GroupBox.setMinimumSize(QtCore.QSize(414, 95))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(GroupBox)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setMargin(2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exposureTimeLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exposureTimeLabel.sizePolicy().hasHeightForWidth())
        self.exposureTimeLabel.setSizePolicy(sizePolicy)
        self.exposureTimeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.exposureTimeLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.exposureTimeLabel.setObjectName(_fromUtf8("exposureTimeLabel"))
        self.horizontalLayout.addWidget(self.exposureTimeLabel)
        self.exposureTimeText = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exposureTimeText.sizePolicy().hasHeightForWidth())
        self.exposureTimeText.setSizePolicy(sizePolicy)
        self.exposureTimeText.setMinimumSize(QtCore.QSize(50, 0))
        self.exposureTimeText.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.exposureTimeText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exposureTimeText.setFrameShape(QtGui.QFrame.NoFrame)
        self.exposureTimeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exposureTimeText.setObjectName(_fromUtf8("exposureTimeText"))
        self.horizontalLayout.addWidget(self.exposureTimeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.FPSLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FPSLabel.sizePolicy().hasHeightForWidth())
        self.FPSLabel.setSizePolicy(sizePolicy)
        self.FPSLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.FPSLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.FPSLabel.setObjectName(_fromUtf8("FPSLabel"))
        self.horizontalLayout_4.addWidget(self.FPSLabel)
        self.FPSText = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FPSText.sizePolicy().hasHeightForWidth())
        self.FPSText.setSizePolicy(sizePolicy)
        self.FPSText.setMinimumSize(QtCore.QSize(50, 0))
        self.FPSText.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.FPSText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FPSText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FPSText.setObjectName(_fromUtf8("FPSText"))
        self.horizontalLayout_4.addWidget(self.FPSText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pictureSizeLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureSizeLabel.sizePolicy().hasHeightForWidth())
        self.pictureSizeLabel.setSizePolicy(sizePolicy)
        self.pictureSizeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.pictureSizeLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.pictureSizeLabel.setObjectName(_fromUtf8("pictureSizeLabel"))
        self.horizontalLayout_6.addWidget(self.pictureSizeLabel)
        self.pictureSizeText = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureSizeText.sizePolicy().hasHeightForWidth())
        self.pictureSizeText.setSizePolicy(sizePolicy)
        self.pictureSizeText.setMinimumSize(QtCore.QSize(90, 0))
        self.pictureSizeText.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.pictureSizeText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pictureSizeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pictureSizeText.setObjectName(_fromUtf8("pictureSizeText"))
        self.horizontalLayout_6.addWidget(self.pictureSizeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.temperatureLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatureLabel.sizePolicy().hasHeightForWidth())
        self.temperatureLabel.setSizePolicy(sizePolicy)
        self.temperatureLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.temperatureLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.temperatureLabel.setObjectName(_fromUtf8("temperatureLabel"))
        self.horizontalLayout_2.addWidget(self.temperatureLabel)
        self.temperatureText = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatureText.sizePolicy().hasHeightForWidth())
        self.temperatureText.setSizePolicy(sizePolicy)
        self.temperatureText.setMinimumSize(QtCore.QSize(50, 0))
        self.temperatureText.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.temperatureText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temperatureText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperatureText.setObjectName(_fromUtf8("temperatureText"))
        self.horizontalLayout_2.addWidget(self.temperatureText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.EMCCDLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EMCCDLabel.sizePolicy().hasHeightForWidth())
        self.EMCCDLabel.setSizePolicy(sizePolicy)
        self.EMCCDLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.EMCCDLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.EMCCDLabel.setObjectName(_fromUtf8("EMCCDLabel"))
        self.horizontalLayout_3.addWidget(self.EMCCDLabel)
        self.EMCCDSlider = QtGui.QSlider(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EMCCDSlider.sizePolicy().hasHeightForWidth())
        self.EMCCDSlider.setSizePolicy(sizePolicy)
        self.EMCCDSlider.setMinimumSize(QtCore.QSize(100, 0))
        self.EMCCDSlider.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.EMCCDSlider.setMaximum(100)
        self.EMCCDSlider.setProperty("value", 0)
        self.EMCCDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EMCCDSlider.setObjectName(_fromUtf8("EMCCDSlider"))
        self.horizontalLayout_3.addWidget(self.EMCCDSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.preampGainLabel = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preampGainLabel.sizePolicy().hasHeightForWidth())
        self.preampGainLabel.setSizePolicy(sizePolicy)
        self.preampGainLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.preampGainLabel.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.preampGainLabel.setObjectName(_fromUtf8("preampGainLabel"))
        self.horizontalLayout_5.addWidget(self.preampGainLabel)
        self.preampGainText = QtGui.QLabel(GroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preampGainText.sizePolicy().hasHeightForWidth())
        self.preampGainText.setSizePolicy(sizePolicy)
        self.preampGainText.setMinimumSize(QtCore.QSize(50, 0))
        self.preampGainText.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.preampGainText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.preampGainText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.preampGainText.setObjectName(_fromUtf8("preampGainText"))
        self.horizontalLayout_5.addWidget(self.preampGainText)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        GroupBox.setTitle(_translate("GroupBox", "Camera", None))
        self.exposureTimeLabel.setText(_translate("GroupBox", "Exposure Time (s):", None))
        self.exposureTimeText.setText(_translate("GroupBox", "0", None))
        self.FPSLabel.setText(_translate("GroupBox", "FPS (Hz):", None))
        self.FPSText.setText(_translate("GroupBox", "0", None))
        self.pictureSizeLabel.setText(_translate("GroupBox", "Picture Size:", None))
        self.pictureSizeText.setText(_translate("GroupBox", "0", None))
        self.temperatureLabel.setText(_translate("GroupBox", "Temperature (C):", None))
        self.temperatureText.setText(_translate("GroupBox", "0", None))
        self.EMCCDLabel.setText(_translate("GroupBox", "EMCCD Gain: 0", None))
        self.preampGainLabel.setText(_translate("GroupBox", "Preamp Gain:", None))
        self.preampGainText.setText(_translate("GroupBox", "0", None))

