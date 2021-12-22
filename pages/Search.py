# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchPage(object):
    def setupUi(self, SearchPage):
        SearchPage.setObjectName("SearchPage")
        SearchPage.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchPage.sizePolicy().hasHeightForWidth())
        SearchPage.setSizePolicy(sizePolicy)
        SearchPage.setMinimumSize(QtCore.QSize(1024, 768))
        SearchPage.setStyleSheet("background-color: rgb(98, 160, 234);\n"
"background-color: rgb(153, 193, 241);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(SearchPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(370, 320, 268, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NID1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NID1.sizePolicy().hasHeightForWidth())
        self.NID1.setSizePolicy(sizePolicy)
        self.NID1.setObjectName("NID1")
        self.gridLayout.addWidget(self.NID1, 1, 0, 1, 1)
        self.search = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        SearchPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SearchPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchPage)
        self.statusbar.setObjectName("statusbar")
        SearchPage.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(SearchPage)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SearchPage)
        QtCore.QMetaObject.connectSlotsByName(SearchPage)

    def retranslateUi(self, SearchPage):
        _translate = QtCore.QCoreApplication.translate
        SearchPage.setWindowTitle(_translate("SearchPage", "MainWindow"))
        self.search.setText(_translate("SearchPage", "Search"))
        self.label.setText(_translate("SearchPage", "Enter National ID Number "))
        self.menuFile.setTitle(_translate("SearchPage", "File"))
        self.actionClose.setText(_translate("SearchPage", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchPage = QtWidgets.QMainWindow()
    ui = Ui_SearchPage()
    ui.setupUi(SearchPage)
    SearchPage.show()
    sys.exit(app.exec_())
