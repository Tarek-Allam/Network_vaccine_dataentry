# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewPage(object):
    def setupUi(self, ViewPage):
        ViewPage.setObjectName("ViewPage")
        ViewPage.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewPage.sizePolicy().hasHeightForWidth())
        ViewPage.setSizePolicy(sizePolicy)
        ViewPage.setMinimumSize(QtCore.QSize(1024, 768))
        ViewPage.setStyleSheet("background-color: rgb(248, 228, 92);\n"
"background-color: rgb(98, 160, 234);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(ViewPage)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 230, 285, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.nid = QtWidgets.QLabel(self.layoutWidget)
        self.nid.setText("")
        self.nid.setObjectName("nid")
        self.gridLayout.addWidget(self.nid, 1, 1, 1, 1)
        self.name = QtWidgets.QLabel(self.layoutWidget)
        self.name.setText("")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)
        self.vaccine_name = QtWidgets.QLabel(self.layoutWidget)
        self.vaccine_name.setText("")
        self.vaccine_name.setObjectName("vaccine_name")
        self.gridLayout.addWidget(self.vaccine_name, 3, 1, 1, 1)
        self.vaccine_code = QtWidgets.QLabel(self.layoutWidget)
        self.vaccine_code.setText("")
        self.vaccine_code.setObjectName("vaccine_code")
        self.gridLayout.addWidget(self.vaccine_code, 4, 1, 1, 1)
        self.status = QtWidgets.QLabel(self.layoutWidget)
        self.status.setText("")
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 5, 1, 1, 1)
        ViewPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ViewPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewPage)
        self.statusbar.setObjectName("statusbar")
        ViewPage.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(ViewPage)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ViewPage)
        QtCore.QMetaObject.connectSlotsByName(ViewPage)

    def retranslateUi(self, ViewPage):
        _translate = QtCore.QCoreApplication.translate
        ViewPage.setWindowTitle(_translate("ViewPage", "MainWindow"))
        self.label_3.setText(_translate("ViewPage", "Name"))
        self.label_4.setText(_translate("ViewPage", "Vaccine Code"))
        self.label_2.setText(_translate("ViewPage", "Vaccince Name"))
        self.label.setText(_translate("ViewPage", "National ID Number "))
        self.label_5.setText(_translate("ViewPage", "Status"))
        self.label_6.setText(_translate("ViewPage", "User Data is"))
        self.menuFile.setTitle(_translate("ViewPage", "File"))
        self.actionClose.setText(_translate("ViewPage", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewPage = QtWidgets.QMainWindow()
    ui = Ui_ViewPage()
    ui.setupUi(ViewPage)
    ViewPage.show()
    sys.exit(app.exec_())
