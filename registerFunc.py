import sys
from register import Ui_LoginForm
import mainAppFunc
from customQDialog import CustomDialogWarning
from PyQt6.QtWidgets import QWidget, QApplication, QDialog


class LoginForm(QWidget):
    def __init__(self, client):
        super(LoginForm, self).__init__()
        self.client = client
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        self.ui.notRegisteredBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signupPage))
        self.ui.registeredBtn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage))

        self.ui.loginBtn.clicked.connect(
            lambda: self.login())
        self.ui.registerBtn.clicked.connect(
            lambda: self.register())

    def register(self):
        email = self.ui.emailLineEdit.text()
        login = self.ui.nicknameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if self.client.checkEmail(email) == "Exist":
            dlg = CustomDialogWarning("This email already exists!")
            dlg.exec()
        else:
            self.client.addNewUser(email, login, password)
            if self.client.checkEmail(email) == "Exist":
                LoginForm.close(self)
                mainAppFunc.showMainApp(self.client, login)

    def login(self):
        login = self.ui.nicknameLineEdit_2.text()
        password = self.ui.passwordLineEdit_2.text()

        if self.client.checkUser(login, password) == "Exist":
            LoginForm.close(self)
            mainAppFunc.showMainApp(self.client, login)
        else:
            dlg = CustomDialogWarning("There is no such user!")
            dlg.exec()


def showLoginForm(client):
    app = QApplication(sys.argv)
    login_form = LoginForm(client)
    login_form.show()
    if app.exec():
        client.sender(message_type="disconnect", message="disconnect")
        sys.exit()
