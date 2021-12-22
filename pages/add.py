# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPage(object):
    def setupUi(self, AddPage):
        AddPage.setObjectName("AddPage")
        AddPage.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddPage.sizePolicy().hasHeightForWidth())
        AddPage.setSizePolicy(sizePolicy)
        AddPage.setMinimumSize(QtCore.QSize(1024, 768))
        AddPage.setStyleSheet("background-color: rgb(248, 228, 92);\n"
"background-color: rgb(98, 160, 234);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(AddPage)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 230, 285, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.vac_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.vac_name.setObjectName("vac_name")
        self.gridLayout.addWidget(self.vac_name, 2, 1, 1, 1)
        self.add_record = QtWidgets.QPushButton(self.layoutWidget)
        self.add_record.setObjectName("add_record")
        self.gridLayout.addWidget(self.add_record, 5, 0, 1, 2)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.NID2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.NID2.setObjectName("NID2")
        self.gridLayout.addWidget(self.NID2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.vac_code = QtWidgets.QLineEdit(self.layoutWidget)
        self.vac_code.setObjectName("vac_code")
        self.gridLayout.addWidget(self.vac_code, 3, 1, 1, 1)
        self.status = QtWidgets.QLineEdit(self.layoutWidget)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 4, 1, 1, 1)
        AddPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        AddPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddPage)
        self.statusbar.setObjectName("statusbar")
        AddPage.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(AddPage)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(AddPage)
        QtCore.QMetaObject.connectSlotsByName(AddPage)

    def retranslateUi(self, AddPage):
        _translate = QtCore.QCoreApplication.translate
        AddPage.setWindowTitle(_translate("AddPage", "MainWindow"))
        self.add_record.setText(_translate("AddPage", "Add Rescord"))
        self.label.setText(_translate("AddPage", "National ID Number "))
        self.label_5.setText(_translate("AddPage", "Status"))
        self.label_3.setText(_translate("AddPage", "Name"))
        self.label_4.setText(_translate("AddPage", "Vaccine Code"))
        self.label_2.setText(_translate("AddPage", "Vaccince Name"))
        self.menuFile.setTitle(_translate("AddPage", "File"))
        self.actionClose.setText(_translate("AddPage", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPage = QtWidgets.QMainWindow()
    ui = Ui_AddPage()
    ui.setupUi(AddPage)
    AddPage.show()
    sys.exit(app.exec_())
