# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui4_dialog_showalltask.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_showalltask(object):
    def setupUi(self, Dialog_showalltask):
        Dialog_showalltask.setObjectName("Dialog_showalltask")
        Dialog_showalltask.resize(1325, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/todaytaskwindow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_showalltask.setWindowIcon(icon)
        Dialog_showalltask.setStatusTip("")
        Dialog_showalltask.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tasktable = QtWidgets.QTableWidget(Dialog_showalltask)
        self.tasktable.setEnabled(True)
        self.tasktable.setGeometry(QtCore.QRect(0, 0, 1321, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasktable.sizePolicy().hasHeightForWidth())
        self.tasktable.setSizePolicy(sizePolicy)
        self.tasktable.setFrameShape(QtWidgets.QFrame.Panel)
        self.tasktable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tasktable.setLineWidth(1)
        self.tasktable.setMidLineWidth(0)
        self.tasktable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tasktable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tasktable.setAutoScroll(False)
        self.tasktable.setAutoScrollMargin(0)
        self.tasktable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tasktable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tasktable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tasktable.setGridStyle(QtCore.Qt.SolidLine)
        self.tasktable.setRowCount(15)
        self.tasktable.setColumnCount(23)
        self.tasktable.setObjectName("tasktable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.tasktable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.tasktable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.tasktable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tasktable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("方正兰亭黑_GBK")
        font.setStrikeOut(False)
        item.setFont(font)
        self.tasktable.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasktable.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tasktable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("方正兰亭黑_GBK")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tasktable.setItem(0, 15, item)
        self.tasktable.horizontalHeader().setHighlightSections(True)
        self.tasktable.horizontalHeader().setSortIndicatorShown(True)
        self.tasktable.verticalHeader().setVisible(False)
        self.tasktable.verticalHeader().setCascadingSectionResizes(False)
        self.tasktable.verticalHeader().setHighlightSections(False)
        self.tasktable.verticalHeader().setSortIndicatorShown(False)
        self.tasktable.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Dialog_showalltask)
        QtCore.QMetaObject.connectSlotsByName(Dialog_showalltask)

    def retranslateUi(self, Dialog_showalltask):
        _translate = QtCore.QCoreApplication.translate
        Dialog_showalltask.setWindowTitle(_translate("Dialog_showalltask", "Dialog"))
        self.tasktable.setSortingEnabled(True)
        item = self.tasktable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_showalltask", "任务名称"))
        item = self.tasktable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_showalltask", "周一数量"))
        item = self.tasktable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_showalltask", "周一送检时间"))
        item = self.tasktable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_showalltask", "周一取件时间"))
        item = self.tasktable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_showalltask", "周二数量"))
        item = self.tasktable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_showalltask", "周二送检时间"))
        item = self.tasktable.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_showalltask", "周二取件时间"))
        item = self.tasktable.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_showalltask", "周三数量"))
        item = self.tasktable.horizontalHeaderItem(8)
        item.setText(_translate("Dialog_showalltask", "周三送检时间"))
        item = self.tasktable.horizontalHeaderItem(9)
        item.setText(_translate("Dialog_showalltask", "周三取件时间"))
        item = self.tasktable.horizontalHeaderItem(10)
        item.setText(_translate("Dialog_showalltask", "周四数量"))
        item = self.tasktable.horizontalHeaderItem(11)
        item.setText(_translate("Dialog_showalltask", "周四送检时间"))
        item = self.tasktable.horizontalHeaderItem(12)
        item.setText(_translate("Dialog_showalltask", "周四取件时间"))
        item = self.tasktable.horizontalHeaderItem(13)
        item.setText(_translate("Dialog_showalltask", "周五数量"))
        item = self.tasktable.horizontalHeaderItem(14)
        item.setText(_translate("Dialog_showalltask", "周五送检时间"))
        item = self.tasktable.horizontalHeaderItem(15)
        item.setText(_translate("Dialog_showalltask", "周五取件时间"))
        item = self.tasktable.horizontalHeaderItem(16)
        item.setText(_translate("Dialog_showalltask", "周六数量"))
        item = self.tasktable.horizontalHeaderItem(17)
        item.setText(_translate("Dialog_showalltask", "周六数量"))
        item = self.tasktable.horizontalHeaderItem(18)
        item.setText(_translate("Dialog_showalltask", "周六送检时间"))
        item = self.tasktable.horizontalHeaderItem(19)
        item.setText(_translate("Dialog_showalltask", "周六取件时间"))
        item = self.tasktable.horizontalHeaderItem(20)
        item.setText(_translate("Dialog_showalltask", "周日数量"))
        item = self.tasktable.horizontalHeaderItem(21)
        item.setText(_translate("Dialog_showalltask", "周日送检时间"))
        item = self.tasktable.horizontalHeaderItem(22)
        item.setText(_translate("Dialog_showalltask", "周日取件时间"))
        __sortingEnabled = self.tasktable.isSortingEnabled()
        self.tasktable.setSortingEnabled(False)
        self.tasktable.setSortingEnabled(__sortingEnabled)
