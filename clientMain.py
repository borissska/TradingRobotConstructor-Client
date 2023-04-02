import sys
import socket
import json

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu
from mainApp import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.parametersListWidget.installEventFilter(self)

        # mainStackedWidget
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.homeWidget)
        self.ui.homeBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.homeWidget))
        self.ui.myStrategiesBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.myStrategiesWidget))
        self.ui.newStrategyBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.newStrategyWidget))
        self.ui.accountBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.accountWidget))

        # testStrategyBtnClick
        self.ui.testStrategyBtn.clicked.connect(lambda: self.sendTestStrategyData())

        # parameterStackedWidget
        self.ui.parameterStackedWidget.setCurrentWidget(self.ui.disbalanceWidget)
        self.ui.parameterSelectionComboBox.currentTextChanged.connect(self.chooseParameterStackedWidget)

        # changeParameterBtn
        self.ui.changeParameterBtn.clicked.connect(self.changeEnableOfParametersList)

        # changingOfWeightBtn
        self.ui.yesChangingOfWeightBtn.clicked.connect(self.yesBtnChoose)
        self.ui.noChangingOfWeightBtn.clicked.connect(self.noBtnChoose)

        self.ui.addParameterBtn.clicked.connect(self.createParameter)

    def eventFilter(self, source, e):
        if e.type() == QEvent.Type.ContextMenu and source is self.ui.parametersListWidget:
            menu = QMenu(self)
            menu.addAction('Change')
            menu.addAction('Delete')

            # menu.triggered.connect(self.ui.parametersListWidget.selected)

            if menu.exec(e.globalPos()):
                self.item = source.itemAt(e.pos())
            return True
        return super().eventFilter(source, e)

    def createParameter(self):
        if self.ui.parameterSelectionComboBox.currentText() == "Disbalance":
            self.ui.parametersListWidget.addItem(
                f"{self.ui.parameterSelectionComboBox.currentText()}"
                f"(percent:{self.ui.candleBodyPercentageSlider.value()}; "
                f"decreasing:{self.ui.yesChangingOfWeightBtn.isChecked()}; "
                f"weight:{self.ui.weightSlider.value()}; "
                f"interval:{self.ui.intervalSelectionComboBox.currentText()})")

    # function which helps with enabling or disabling parametersListWidget
    def changeEnableOfParametersList(self):
        if self.ui.parametersListWidget.isEnabled():
            self.ui.parametersListWidget.setEnabled(False)
        else:
            self.ui.parametersListWidget.setEnabled(True)

    # function which helps with choosing parameter widgets
    def chooseParameterStackedWidget(self):
        if self.ui.parameterSelectionComboBox.currentText() == "Disbalance":
            self.ui.parameterStackedWidget.setCurrentWidget(self.ui.disbalanceWidget)
        elif self.ui.parameterSelectionComboBox.currentText() == "Fib Div":
            self.ui.parameterStackedWidget.setCurrentWidget(self.ui.page_2)

    def yesBtnChoose(self):
        if self.ui.yesChangingOfWeightBtn.isChecked():
            self.ui.noChangingOfWeightBtn.setChecked(False)

    def noBtnChoose(self):
        if self.ui.noChangingOfWeightBtn.isChecked():
            self.ui.yesChangingOfWeightBtn.setChecked(False)

    def sendTestStrategyData(self):
        list_items = [self.ui.parametersListWidget.item(row).text() for row in
                      range(self.ui.parametersListWidget.count())]

        json_list = {"testStrategy": list_items}
        sock.send(json.dumps(json_list).encode('utf-8'))


if __name__ == "__main__":

    sock = socket.socket()
    sock.connect(('localhost', 9091))

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    if app.exec():
        sock.close()
        sys.exit()
