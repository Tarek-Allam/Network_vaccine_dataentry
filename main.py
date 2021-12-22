import sys

from PyQt5 import QtWidgets

from client import Client
from common.helpers import get_local_ip
from pages.Search import Ui_SearchPage
from pages.add import Ui_AddPage
from pages.view import Ui_ViewPage


class UiManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiManager, self).__init__()
        server_ip = get_local_ip()
        server_port = 8080
        self.search_page = Ui_SearchPage()
        self.add_page = Ui_AddPage()
        self.view_page = Ui_ViewPage()

        self.search_page.setupUi(self)
        self.client = Client(server_ip, server_port)
        self.register_buttons()

    def register_buttons(self):
        self.search_page.search.clicked.connect(self.search_by_nid)
        self.search_page.actionClose.triggered.connect(self.close)

    def search_by_nid(self):
        nid = self.search_page.NID1.text()
        server_response = self.client.find_record(nid)
        if server_response == "User not found":
            self.add_page.setupUi(self)
            self.add_page.add_record.clicked.connect(self.add_user_data)
            self.add_page.actionClose.triggered.connect(self.close)
        else:
            server_response = server_response.split(",")
            self.view_page.setupUi(self)
            self.view_page.nid.setText(server_response[0])
            self.view_page.name.setText(server_response[1])
            self.view_page.vaccine_code.setText(server_response[2])
            self.view_page.vaccine_name.setText(server_response[3])
            self.view_page.status.setText(server_response[4])
            self.view_page.actionClose.triggered.connect(self.close)

    def add_user_data(self):
        nid = self.add_page.NID2.text()
        name = self.add_page.name.text()
        vaccine_code = self.add_page.vac_code.text()
        vaccine_name = self.add_page.vac_name.text()
        status = self.add_page.status.text()
        test_response = self.client.create_record((nid, name, vaccine_code, vaccine_name, status))
        print(test_response)
        if test_response == 'added successfully':
            self.view_page.setupUi(self)
            self.view_page.nid.setText(nid)
            self.view_page.name.setText(name)
            self.view_page.vaccine_code.setText(vaccine_code)
            self.view_page.vaccine_name.setText(vaccine_name)
            self.view_page.status.setText(status)

    def __del__(self):
        print("Close Client GUI Window")
        self.client.close_connection()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiManager()
    MainWindow.show()
    sys.exit(app.exec_())
