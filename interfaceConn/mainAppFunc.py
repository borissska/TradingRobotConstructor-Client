import os

from PyQt6.QtCore import QEvent
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMenu

from interfaceConn.customQDialog import CustomDialogWarning
from interfaces.mainApp import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, client, login):
        super(MainWindow, self).__init__()
        self.login = login
        self.client = client
        self.strategy_names = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loginLbl.setText(f"{self.login}")

        self.ui.parametersListWidget.installEventFilter(self)

        # mainStackedWidget
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.homeWidget)
        self.ui.homeBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.homeWidget))
        self.ui.myStrategiesBtn.clicked.connect(
            lambda: self.updateStrategies())
        self.ui.newStrategyBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.newStrategyWidget))
        self.ui.accountBtn.clicked.connect(
            lambda: self.ui.mainStackedWidget.setCurrentWidget(self.ui.accountWidget))

        # testStrategyBtnClick
        self.ui.testStrategyBtn.clicked.connect(
            lambda: self.sendTestStrategyData())

        # parameterStackedWidget
        self.ui.parameterStackedWidget.setCurrentWidget(self.ui.disbalanceWidget)
        self.ui.parameterSelectionComboBox.currentTextChanged.connect(self.chooseParameterStackedWidget)

        # changeParameterBtn
        self.ui.changeParameterBtn.clicked.connect(self.changeEnableOfParametersList)

        # changingOfWeightBtn
        self.ui.yesChangingOfWeightBtn.clicked.connect(self.yesBtnChoose)
        self.ui.noChangingOfWeightBtn.clicked.connect(self.noBtnChoose)

        self.ui.addParameterBtn.clicked.connect(self.addElement)

        self.ui.marketConnectBtn.clicked.connect(self.addMarket)
        #

    def addMarket(self):
        if self.ui.marketChooseComboBox.currentText() == "Bybit":
            if (self.ui.secretAPILineEdit.text() is not None) and (self.ui.keyAPILineEdit.text() is not None):
                balance = self.client.checkMarketData(market=self.ui.marketChooseComboBox.currentText(),
                                                      key=self.ui.keyAPILineEdit.text(),
                                                      secret=self.ui.secretAPILineEdit.text())
                if balance is not None:
                    self.ui.capitalLbl.setText(f"{balance}")
                else:
                    CustomDialogWarning("The data entered is incorrect!")

    def updateStrategies(self):
        strategies = self.client.updateStrategies(self.login)
        for el in strategies:
            if el[0] not in self.strategy_names:
                path = f"C:\diplomeProject\clientApp\icons\{el[0]}.png"
                if os.path.exists(path):
                    self.addNewStrategy(user_name=self.login, strategy_name=el[0], current_profit=el[1],
                                        percent_of_capital=el[2], max_loss=el[3], full_profit=el[4],
                                        profit_per_year=el[5], state=el[6])
                    self.strategy_names.append(el[0])

        self.ui.mainStackedWidget.setCurrentWidget(self.ui.myStrategiesWidget)

    def eventFilter(self, source, e):
        if e.type() == QEvent.Type.ContextMenu and source is self.ui.parametersListWidget:
            menu = QMenu(self)
            menu.addAction('Change')
            menu.addAction('Delete')

            menu.triggered.connect(self.ui.parametersListWidget.selectedItems)

            if menu.exec(e.globalPos()):
                self.item = source.itemAt(e.pos())
            return True
        return super().eventFilter(source, e)

    def addElement(self):
        if self.ui.parameterSelectionComboBox.currentText() == "Disbalance":
            self.ui.parametersListWidget.addItem(
                f"{self.ui.parameterSelectionComboBox.currentText()}"
                f"(percent:{self.ui.candleBodyPercentageSlider.value()}; "
                f"decreasing:{self.ui.yesChangingOfWeightBtn.isChecked()}; "
                f"weight:{self.ui.weightSlider.value()}; "
                f"interval:{self.ui.intervalSelectionComboBox.currentText()})")
        elif self.ui.parameterSelectionComboBox.currentText() == "SMA":
            if self.isValid(self.ui.periodSMALineEdit.text(), 10, 200, "Period"):
                self.ui.parametersListWidget.addItem(
                    f"{self.ui.parameterSelectionComboBox.currentText()}"
                    f"(period:{self.ui.periodSMALineEdit.text()}; "
                    f"weight:{self.ui.weightSlider.value()}; "
                    f"interval:{self.ui.intervalSelectionComboBox.currentText()})")
        elif self.ui.parameterSelectionComboBox.currentText() == "RSI":
            if self.isValid(self.ui.sellPriceLineEdit.text(), 50, 100, "Sell value"):
                if self.isValid(self.ui.buyPriceLineEdit.text(), 0, 50, "Buy value"):
                    self.ui.parametersListWidget.addItem(
                        f"{self.ui.parameterSelectionComboBox.currentText()}"
                        f"(sell:{self.ui.sellPriceLineEdit.text()}; "
                        f"buy:{self.ui.buyPriceLineEdit.text()}; "
                        f"weight:{self.ui.weightSlider.value()}; "
                        f"interval:{self.ui.intervalSelectionComboBox.currentText()})")
        elif self.ui.parameterSelectionComboBox.currentText() == "EMA":
            if self.isValid(self.ui.periodEMALineEdit.text(), 10, 200, "Period"):
                self.ui.parametersListWidget.addItem(
                    f"{self.ui.parameterSelectionComboBox.currentText()}"
                    f"(period:{self.ui.periodEMALineEdit.text()}; "
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
        elif self.ui.parameterSelectionComboBox.currentText() == "SMA":
            self.ui.parameterStackedWidget.setCurrentWidget(self.ui.smaWidget)
        elif self.ui.parameterSelectionComboBox.currentText() == "RSI":
            self.ui.parameterStackedWidget.setCurrentWidget(self.ui.rsiWidget)
        elif self.ui.parameterSelectionComboBox.currentText() == "EMA":
            self.ui.parameterStackedWidget.setCurrentWidget(self.ui.emaWidget)

    def yesBtnChoose(self):
        if self.ui.yesChangingOfWeightBtn.isChecked():
            self.ui.noChangingOfWeightBtn.setChecked(False)

    def noBtnChoose(self):
        if self.ui.noChangingOfWeightBtn.isChecked():
            self.ui.yesChangingOfWeightBtn.setChecked(False)

    def sendTestStrategyData(self):
        if self.ui.parametersListWidget.count() > 0:
            list_items = [self.ui.parametersListWidget.item(row).text() for row in
                          range(self.ui.parametersListWidget.count())]
            if self.isValid(self.ui.leverageLineEdit.text(), 1, 10, "Leverage"):
                if self.isValid(self.ui.percentofCapitalLineEdit.text(), 1, 100, "Percent of capital"):
                    json_list = {"user_name": self.ui.loginLbl.text(),
                                 "ticker": self.ui.tickerSelectionComboBox.currentText(),
                                 "leverage": self.ui.leverageLineEdit.text(),
                                 "percent_of_capital": self.ui.percentofCapitalLineEdit.text(),
                                 "strategy_name": self.ui.strategyNameLineEdit.text(),
                                 "test_strategy": list_items}
                    self.client.sendTestStrategyData(json_list)
        else:
            dlg = CustomDialogWarning("There are no elements in strategy!")
            dlg.exec()
            return

    def deleteStrategy(self, user_name, strategy_name):
        print(strategy_name)
        child = self.ui.scrollAreaWidgetContents.findChild(QtWidgets.QFrame, f"{strategy_name}")
        child.deleteLater()
        pass

    def changeStrategyState(self, state, strategy_name):
        print(f"{state}")
        child = self.ui.scrollAreaWidgetContents.findChild(QtWidgets.QFrame, f"{strategy_name}")
        label = child.findChild(QtWidgets.QLabel, "stateLbl")
        label.setText(f"State: {state}")

    @staticmethod
    def isValid(value, bottom, top, name):
        if not value.isdigit():
            dlg = CustomDialogWarning(f"{name} is not digit!")
            dlg.exec()
            return False
        else:
            int_value = int(value)
            correct_value = max(bottom, min(int_value, top))
            if correct_value != int_value:
                dlg = CustomDialogWarning(f"{name} is not between {bottom} and {top}!")
                dlg.exec()
                return False
            else:
                return True

    def addNewStrategy(self, *, user_name, strategy_name, current_profit, percent_of_capital, max_loss, full_profit,
                       profit_per_year, state):
        font = QtGui.QFont()
        font.setPointSize(14)
        _translate = QtCore.QCoreApplication.translate

        self.ui.strategyOne = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.strategyOne.sizePolicy().hasHeightForWidth())
        self.ui.strategyOne.setSizePolicy(sizePolicy)
        self.ui.strategyOne.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.ui.strategyOne.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui.strategyOne.setObjectName(f"{strategy_name}")
        self.ui.verticalLayout_17 = QtWidgets.QVBoxLayout(self.ui.strategyOne)
        self.ui.verticalLayout_17.setObjectName("verticalLayout_17")
        self.ui.strategyNameWidget = QtWidgets.QWidget(self.ui.strategyOne)
        self.ui.strategyNameWidget.setObjectName("strategyNameWidget")
        self.ui.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ui.strategyNameWidget)
        self.ui.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ui.strategyNameLbl_2 = QtWidgets.QLabel(self.ui.strategyNameWidget)

        self.ui.strategyNameLbl_2.setFont(font)
        self.ui.strategyNameLbl_2.setObjectName("strategyNameLbl_2")
        self.ui.horizontalLayout_6.addWidget(self.ui.strategyNameLbl_2)
        self.ui.verticalLayout_17.addWidget(self.ui.strategyNameWidget, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.ui.dataFeedLbl = QtWidgets.QLabel(self.ui.strategyOne)
        self.ui.pixmap = QtGui.QPixmap(f'icons/{strategy_name}.png')
        self.ui.pixmap = self.ui.pixmap.scaled(1050, 1000, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.dataFeedLbl.setPixmap(self.ui.pixmap)
        self.ui.dataFeedLbl.setStyleSheet(f"background-image:url(:icons/{strategy_name}.png)")
        self.ui.dataFeedLbl.setScaledContents(True)
        self.ui.dataFeedLbl.setObjectName("dataFeedLbl")
        self.ui.verticalLayout_17.addWidget(self.ui.dataFeedLbl)
        self.ui.strategyBtnsWidget = QtWidgets.QWidget(self.ui.strategyOne)
        self.ui.strategyBtnsWidget.setObjectName("strategyBtnsWidget")
        self.ui.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ui.strategyBtnsWidget)
        self.ui.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ui.deleteStrategyBtn = QtWidgets.QPushButton(self.ui.strategyBtnsWidget)
        self.ui.deleteStrategyBtn.setFont(font)
        self.ui.deleteStrategyBtn.setObjectName("deleteStrategyBtn")
        self.ui.deleteStrategyBtn.clicked.connect(lambda: self.deleteStrategy(user_name, strategy_name))
        self.ui.horizontalLayout_7.addWidget(self.ui.deleteStrategyBtn)
        self.ui.stopStrategyBtn = QtWidgets.QPushButton(self.ui.strategyBtnsWidget)
        self.ui.stopStrategyBtn.setFont(font)
        self.ui.stopStrategyBtn.setObjectName("stopStrategyBtn")
        self.ui.stopStrategyBtn.clicked.connect(lambda: self.changeStrategyState("stopped", strategy_name))
        self.ui.horizontalLayout_7.addWidget(self.ui.stopStrategyBtn)
        self.ui.runStrategyBtn = QtWidgets.QPushButton(self.ui.strategyBtnsWidget)
        self.ui.runStrategyBtn.setFont(font)
        self.ui.runStrategyBtn.setObjectName("runStrategyBtn")
        self.ui.runStrategyBtn.clicked.connect(lambda: self.changeStrategyState("working", strategy_name))
        self.ui.horizontalLayout_7.addWidget(self.ui.runStrategyBtn)
        self.ui.verticalLayout_17.addWidget(self.ui.strategyBtnsWidget)
        self.ui.strategyStateWidget = QtWidgets.QWidget(self.ui.strategyOne)
        self.ui.strategyStateWidget.setObjectName("strategyStateWidget")
        self.ui.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.ui.strategyStateWidget)
        self.ui.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ui.stateLbl = QtWidgets.QLabel(self.ui.strategyStateWidget)
        self.ui.stateLbl.setFont(font)
        self.ui.stateLbl.setObjectName("stateLbl")
        self.ui.horizontalLayout_8.addWidget(self.ui.stateLbl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.ui.horizontalLayout_8.addItem(spacerItem1)
        self.ui.currentYieldLbl = QtWidgets.QLabel(self.ui.strategyStateWidget)
        self.ui.currentYieldLbl.setFont(font)
        self.ui.currentYieldLbl.setMouseTracking(False)
        self.ui.currentYieldLbl.setAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ui.currentYieldLbl.setObjectName("currentYieldLbl")
        self.ui.horizontalLayout_8.addWidget(self.ui.currentYieldLbl)
        self.ui.verticalLayout_17.addWidget(self.ui.strategyStateWidget)
        self.ui.verticalLayout_13.addWidget(self.ui.strategyOne)

        self.ui.strategyNameLbl_2.setText(_translate("MainWindow", f"Strategy Name: {strategy_name}"))
        self.ui.deleteStrategyBtn.setText(_translate("MainWindow", "Delete Strategy"))
        self.ui.stopStrategyBtn.setText(_translate("MainWindow", "Stop Strategy"))
        self.ui.runStrategyBtn.setText(_translate("MainWindow", "Run Strategy"))
        self.ui.stateLbl.setText(_translate("MainWindow", f"State: {state}"))
        self.ui.currentYieldLbl.setText(_translate("MainWindow", f"Current Yield: {current_profit}"))


def showMainApp(client, login):
    window = MainWindow(client, login)
    window.show()
    client.updateStrategies(login)
