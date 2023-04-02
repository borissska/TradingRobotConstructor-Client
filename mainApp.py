# Form implementation generated from reading ui file 'C:\diplomeProject\clientApp\mainAPP.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 738)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "    text-align: center;\n"
                                 "    padding: 10px;\n"
                                 "}\n"
                                 "")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuContainer = QtWidgets.QWidget(self.centralWidget)
        self.menuContainer.setObjectName("menuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuContainer)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeBtnsContainer = QtWidgets.QFrame(self.menuContainer)
        self.homeBtnsContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.homeBtnsContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.homeBtnsContainer.setObjectName("homeBtnsContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.homeBtnsContainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.homeBtnsContainer)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QtCore.QSize(28, 28))
        self.homeBtn.setObjectName("homeBtn")
        self.horizontalLayout_3.addWidget(self.homeBtn)
        self.verticalLayout.addWidget(self.homeBtnsContainer, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.mainPagesBtnsContainer = QtWidgets.QWidget(self.menuContainer)
        self.mainPagesBtnsContainer.setObjectName("mainPagesBtnsContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainPagesBtnsContainer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.myStrategiesBtn = QtWidgets.QPushButton(self.mainPagesBtnsContainer)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.myStrategiesBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/trending-up.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.myStrategiesBtn.setIcon(icon1)
        self.myStrategiesBtn.setIconSize(QtCore.QSize(24, 24))
        self.myStrategiesBtn.setObjectName("myStrategiesBtn")
        self.verticalLayout_3.addWidget(self.myStrategiesBtn)
        self.newStrategyBtn = QtWidgets.QPushButton(self.mainPagesBtnsContainer)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newStrategyBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.newStrategyBtn.setIcon(icon2)
        self.newStrategyBtn.setIconSize(QtCore.QSize(24, 24))
        self.newStrategyBtn.setObjectName("newStrategyBtn")
        self.verticalLayout_3.addWidget(self.newStrategyBtn)
        self.verticalLayout.addWidget(self.mainPagesBtnsContainer)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.mainAccountBtnsContainer = QtWidgets.QWidget(self.menuContainer)
        self.mainAccountBtnsContainer.setObjectName("mainAccountBtnsContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainAccountBtnsContainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.accountBtn = QtWidgets.QPushButton(self.mainAccountBtnsContainer)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.accountBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.accountBtn.setIcon(icon3)
        self.accountBtn.setIconSize(QtCore.QSize(24, 24))
        self.accountBtn.setObjectName("accountBtn")
        self.verticalLayout_2.addWidget(self.accountBtn)
        self.verticalLayout.addWidget(self.mainAccountBtnsContainer)
        self.horizontalLayout.addWidget(self.menuContainer, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.homeWidget = QtWidgets.QWidget()
        self.homeWidget.setObjectName("homeWidget")
        self.mainStackedWidget.addWidget(self.homeWidget)
        self.myStrategiesWidget = QtWidgets.QWidget()
        self.myStrategiesWidget.setObjectName("myStrategiesWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.myStrategiesWidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.scrollArea = QtWidgets.QScrollArea(self.myStrategiesWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 975, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.strategyOne = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strategyOne.sizePolicy().hasHeightForWidth())
        self.strategyOne.setSizePolicy(sizePolicy)
        self.strategyOne.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.strategyOne.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.strategyOne.setObjectName("strategyOne")
        self.gridLayout = QtWidgets.QGridLayout(self.strategyOne)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.strategyOne)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.strategyOne)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.strategyOne)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.strategyOne)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.strategyOne)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout_13.addWidget(self.strategyOne, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_12.addWidget(self.scrollArea)
        self.mainStackedWidget.addWidget(self.myStrategiesWidget)
        self.newStrategyWidget = QtWidgets.QWidget()
        self.newStrategyWidget.setObjectName("newStrategyWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.newStrategyWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.parameterSelectionHalfWidget = QtWidgets.QWidget(self.newStrategyWidget)
        self.parameterSelectionHalfWidget.setObjectName("parameterSelectionHalfWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.parameterSelectionHalfWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.parameterMainLabelWidget = QtWidgets.QWidget(self.parameterSelectionHalfWidget)
        self.parameterMainLabelWidget.setObjectName("parameterMainLabelWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.parameterMainLabelWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.parameterMainLbl = QtWidgets.QLabel(self.parameterMainLabelWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.parameterMainLbl.setFont(font)
        self.parameterMainLbl.setObjectName("parameterMainLbl")
        self.verticalLayout_5.addWidget(self.parameterMainLbl)
        self.verticalLayout_4.addWidget(self.parameterMainLabelWidget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.parameterSelectionWidget = QtWidgets.QWidget(self.parameterSelectionHalfWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameterSelectionWidget.sizePolicy().hasHeightForWidth())
        self.parameterSelectionWidget.setSizePolicy(sizePolicy)
        self.parameterSelectionWidget.setObjectName("parameterSelectionWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.parameterSelectionWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.parameterSelectionComboBox = QtWidgets.QComboBox(self.parameterSelectionWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parameterSelectionComboBox.setFont(font)
        self.parameterSelectionComboBox.setObjectName("parameterSelectionComboBox")
        self.parameterSelectionComboBox.addItem("")
        self.parameterSelectionComboBox.addItem("")
        self.parameterSelectionComboBox.addItem("")
        self.verticalLayout_7.addWidget(self.parameterSelectionComboBox)
        self.parameterStackedWidget = QtWidgets.QStackedWidget(self.parameterSelectionWidget)
        self.parameterStackedWidget.setObjectName("parameterStackedWidget")
        self.disbalanceWidget = QtWidgets.QWidget()
        self.disbalanceWidget.setObjectName("disbalanceWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.disbalanceWidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.candleBodyPercentageLbl = QtWidgets.QLabel(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.candleBodyPercentageLbl.setFont(font)
        self.candleBodyPercentageLbl.setObjectName("candleBodyPercentageLbl")
        self.verticalLayout_10.addWidget(self.candleBodyPercentageLbl)
        self.candleBodyPercentageSlider = QtWidgets.QSlider(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.candleBodyPercentageSlider.setFont(font)
        self.candleBodyPercentageSlider.setMaximum(100)
        self.candleBodyPercentageSlider.setSliderPosition(80)
        self.candleBodyPercentageSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.candleBodyPercentageSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.candleBodyPercentageSlider.setTickInterval(2)
        self.candleBodyPercentageSlider.setObjectName("candleBodyPercentageSlider")
        self.verticalLayout_10.addWidget(self.candleBodyPercentageSlider)
        self.changingOfWeightLbl = QtWidgets.QLabel(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.changingOfWeightLbl.setFont(font)
        self.changingOfWeightLbl.setObjectName("changingOfWeightLbl")
        self.verticalLayout_10.addWidget(self.changingOfWeightLbl)
        self.label = QtWidgets.QLabel(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.yesChangingOfWeightBtn = QtWidgets.QRadioButton(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yesChangingOfWeightBtn.setFont(font)
        self.yesChangingOfWeightBtn.setChecked(True)
        self.yesChangingOfWeightBtn.setObjectName("yesChangingOfWeightBtn")
        self.verticalLayout_10.addWidget(self.yesChangingOfWeightBtn)
        self.noChangingOfWeightBtn = QtWidgets.QRadioButton(self.disbalanceWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.noChangingOfWeightBtn.setFont(font)
        self.noChangingOfWeightBtn.setObjectName("noChangingOfWeightBtn")
        self.verticalLayout_10.addWidget(self.noChangingOfWeightBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.parameterStackedWidget.addWidget(self.disbalanceWidget)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.parameterStackedWidget.addWidget(self.page_2)
        self.verticalLayout_7.addWidget(self.parameterStackedWidget, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.weightWidget = QtWidgets.QWidget(self.parameterSelectionWidget)
        self.weightWidget.setObjectName("weightWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.weightWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.weightLbl = QtWidgets.QLabel(self.weightWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weightLbl.setFont(font)
        self.weightLbl.setObjectName("weightLbl")
        self.verticalLayout_9.addWidget(self.weightLbl)
        self.weightSlider = QtWidgets.QSlider(self.weightWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weightSlider.setFont(font)
        self.weightSlider.setAutoFillBackground(False)
        self.weightSlider.setMinimum(-10)
        self.weightSlider.setMaximum(10)
        self.weightSlider.setProperty("value", 0)
        self.weightSlider.setSliderPosition(0)
        self.weightSlider.setTracking(True)
        self.weightSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.weightSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.weightSlider.setTickInterval(1)
        self.weightSlider.setObjectName("weightSlider")
        self.verticalLayout_9.addWidget(self.weightSlider)
        self.verticalLayout_7.addWidget(self.weightWidget)
        self.intervatSelectionWidget = QtWidgets.QWidget(self.parameterSelectionWidget)
        self.intervatSelectionWidget.setObjectName("intervatSelectionWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.intervatSelectionWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.intervalSelectionLbl = QtWidgets.QLabel(self.intervatSelectionWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.intervalSelectionLbl.setFont(font)
        self.intervalSelectionLbl.setObjectName("intervalSelectionLbl")
        self.verticalLayout_6.addWidget(self.intervalSelectionLbl)
        self.intervalSelectionComboBox = QtWidgets.QComboBox(self.intervatSelectionWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.intervalSelectionComboBox.setFont(font)
        self.intervalSelectionComboBox.setObjectName("intervalSelectionComboBox")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.intervalSelectionComboBox.addItem("")
        self.verticalLayout_6.addWidget(self.intervalSelectionComboBox)
        self.verticalLayout_7.addWidget(self.intervatSelectionWidget)
        self.btnsWidget = QtWidgets.QWidget(self.parameterSelectionWidget)
        self.btnsWidget.setObjectName("btnsWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.btnsWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.changeParameterBtn = QtWidgets.QPushButton(self.btnsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.changeParameterBtn.setFont(font)
        self.changeParameterBtn.setObjectName("changeParameterBtn")
        self.horizontalLayout_5.addWidget(self.changeParameterBtn)
        self.addParameterBtn = QtWidgets.QPushButton(self.btnsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addParameterBtn.setFont(font)
        self.addParameterBtn.setObjectName("addParameterBtn")
        self.horizontalLayout_5.addWidget(self.addParameterBtn)
        self.verticalLayout_7.addWidget(self.btnsWidget)
        self.verticalLayout_4.addWidget(self.parameterSelectionWidget)
        self.horizontalLayout_2.addWidget(self.parameterSelectionHalfWidget)
        self.strategyViewTaxtHalfWidget = QtWidgets.QWidget(self.newStrategyWidget)
        self.strategyViewTaxtHalfWidget.setObjectName("strategyViewTaxtHalfWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.strategyViewTaxtHalfWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.parametersListWidget = QtWidgets.QListWidget(self.strategyViewTaxtHalfWidget)
        self.parametersListWidget.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parametersListWidget.setFont(font)
        self.parametersListWidget.setObjectName("parametersListWidget")
        self.verticalLayout_8.addWidget(self.parametersListWidget)
        self.testStrategyBtnWidget = QtWidgets.QWidget(self.strategyViewTaxtHalfWidget)
        self.testStrategyBtnWidget.setObjectName("testStrategyBtnWidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.testStrategyBtnWidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget = QtWidgets.QWidget(self.testStrategyBtnWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_15.addWidget(self.lineEdit)
        self.verticalLayout_14.addWidget(self.widget)
        self.testStrategyBtn = QtWidgets.QPushButton(self.testStrategyBtnWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.testStrategyBtn.setFont(font)
        self.testStrategyBtn.setObjectName("testStrategyBtn")
        self.verticalLayout_14.addWidget(self.testStrategyBtn)
        self.verticalLayout_8.addWidget(self.testStrategyBtnWidget)
        self.horizontalLayout_2.addWidget(self.strategyViewTaxtHalfWidget)
        self.mainStackedWidget.addWidget(self.newStrategyWidget)
        self.accountWidget = QtWidgets.QWidget()
        self.accountWidget.setObjectName("accountWidget")
        self.mainStackedWidget.addWidget(self.accountWidget)
        self.horizontalLayout.addWidget(self.mainStackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.mainStackedWidget.setCurrentIndex(1)
        self.parameterStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.myStrategiesBtn.setText(_translate("MainWindow", "My Strategies"))
        self.newStrategyBtn.setText(_translate("MainWindow", "New Strategy"))
        self.accountBtn.setText(_translate("MainWindow", "Account"))
        self.label_3.setText(_translate("MainWindow", "Strategy Name: "))
        self.label_4.setText(_translate("MainWindow", "StrtgNm"))
        self.label_5.setText(_translate("MainWindow", "Current Yield: "))
        self.pushButton_2.setText(_translate("MainWindow", "Check Strategy"))
        self.label_6.setText(_translate("MainWindow", "Not Working"))
        self.parameterMainLbl.setText(_translate("MainWindow", "New Strategy"))
        self.parameterSelectionComboBox.setItemText(0, _translate("MainWindow", "Disbalance"))
        self.parameterSelectionComboBox.setItemText(1, _translate("MainWindow", "Fib Div"))
        self.parameterSelectionComboBox.setItemText(2, _translate("MainWindow", "Candle Stick"))
        self.candleBodyPercentageLbl.setText(_translate("MainWindow", "Сandle body percentage"))
        self.changingOfWeightLbl.setText(_translate("MainWindow", "Decrease the weight when moving away from"))
        self.label.setText(_translate("MainWindow", "the current price?"))
        self.yesChangingOfWeightBtn.setText(_translate("MainWindow", "Yes"))
        self.noChangingOfWeightBtn.setText(_translate("MainWindow", "No"))
        self.weightLbl.setText(_translate("MainWindow", "Weight Selection:"))
        self.intervalSelectionLbl.setText(_translate("MainWindow", "Interval Selection:"))
        self.intervalSelectionComboBox.setItemText(0, _translate("MainWindow", "15 min"))
        self.intervalSelectionComboBox.setItemText(1, _translate("MainWindow", "30 min"))
        self.intervalSelectionComboBox.setItemText(2, _translate("MainWindow", "1 hour"))
        self.intervalSelectionComboBox.setItemText(3, _translate("MainWindow", "4 hours"))
        self.intervalSelectionComboBox.setItemText(4, _translate("MainWindow", "12 hours"))
        self.intervalSelectionComboBox.setItemText(5, _translate("MainWindow", "1 day"))
        self.intervalSelectionComboBox.setItemText(6, _translate("MainWindow", "1 week"))
        self.intervalSelectionComboBox.setItemText(7, _translate("MainWindow", "1 month"))
        self.changeParameterBtn.setText(_translate("MainWindow", "Change Parameter"))
        self.addParameterBtn.setText(_translate("MainWindow", "Add Parameter"))
        self.label_2.setText(_translate("MainWindow", "Strategy Name:"))
        self.testStrategyBtn.setText(_translate("MainWindow", "Test Strategy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
