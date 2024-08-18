import sys
import string
import secrets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect your buttons and other widgets here
        self.ui.generateCustomPasswordButton.clicked.connect(self.generate_password)
        self.ui.generateSecureButton.clicked.connect(self.generate_secure_password)
        self.ui.generatePassphraseButton.clicked.connect(self.generate_passphrase_from_existing_password)
        self.ui.generateUserInputButton.clicked.connect(self.generate_password_from_input)

        self.generated_password = ""

    def generate_password(self):
        length = self.ui.lengthSpinBox.value()
        characters = ""
        
        if self.ui.includeUppercase.isChecked():
            characters += string.ascii_uppercase
        if self.ui.includeLowercase.isChecked():
            characters += string.ascii_lowercase
        if self.ui.includeDigits.isChecked():
            characters += string.digits
        if self.ui.includeSymbols.isChecked():
            characters += string.punctuation

        if not characters:
            QMessageBox.warning(self, "Warning", "Please select at least one character type.")
            return

        self.generated_password = ''.join(secrets.choice(characters) for _ in range(length))
        self.show_generated_password(self.generated_password)

    def generate_secure_password(self):
        length = self.ui.secureLengthSpinBox.value()
        characters = string.ascii_letters + string.digits + string.punctuation
        self.generated_password = ''.join(secrets.choice(characters) for _ in range(length))
        self.show_generated_password(self.generated_password)

    def generate_passphrase_from_existing_password(self):
        existing_password = self.ui.existingPasswordField.text().strip()
        if not existing_password:
            QMessageBox.warning(self, "Warning", "Please enter your current password.")
            return

        self.generated_password = self.transform_password(existing_password)
        self.show_generated_password(self.generated_password)

    def transform_password(self, password):
        translation_table = str.maketrans(
            string.ascii_uppercase[:13] + string.ascii_uppercase[13:] + string.ascii_lowercase[:13] + string.ascii_lowercase[13:] + "01234" + "56789",
            string.ascii_lowercase[-13:] + string.ascii_lowercase[:13] + string.ascii_lowercase[-13:] + string.ascii_uppercase[:13] + "56789" + "01234"
        )
        return password.translate(translation_table)

    def generate_password_from_input(self):
        user_input = self.ui.userInputField.text().strip()
        if not user_input:
            QMessageBox.warning(self, "Warning", "Please enter some text to generate a password.")
            return

        self.generated_password = ''.join(secrets.choice(user_input) for _ in range(len(user_input)))
        self.show_generated_password(self.generated_password)

    def show_generated_password(self, password):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Generated Password")
        msg_box.setText(f"Your generated password: {password}")

        # Add the Copy button to the message box
        copy_button = QPushButton("Copy")
        msg_box.addButton(copy_button, QMessageBox.ButtonRole.ActionRole)
        copy_button.clicked.connect(lambda: self.copy_password_to_clipboard(password))

        # Add an OK button to the message box
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        
        msg_box.exec()

    def copy_password_to_clipboard(self, password):
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
        QMessageBox.information(self, "Copied to Clipboard", "The generated password has been copied to the clipboard.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
