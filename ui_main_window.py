# ui_main_window.py

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create the main layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Customizable Password Generator Section
        self.customOptionsLabel = QtWidgets.QLabel("Password Generator with Customizable Options")
        self.verticalLayout.addWidget(self.customOptionsLabel)
        
        self.lengthLabel = QtWidgets.QLabel("Length:")
        self.verticalLayout.addWidget(self.lengthLabel)
        self.lengthSpinBox = QtWidgets.QSpinBox()
        self.lengthSpinBox.setMinimum(6)
        self.lengthSpinBox.setMaximum(128)
        self.lengthSpinBox.setValue(12)
        self.verticalLayout.addWidget(self.lengthSpinBox)

        self.includeUppercase = QtWidgets.QCheckBox("Include Uppercase Letters")
        self.verticalLayout.addWidget(self.includeUppercase)

        self.includeLowercase = QtWidgets.QCheckBox("Include Lowercase Letters")
        self.includeLowercase.setChecked(True)
        self.verticalLayout.addWidget(self.includeLowercase)

        self.includeDigits = QtWidgets.QCheckBox("Include Digits")
        self.includeDigits.setChecked(True)
        self.verticalLayout.addWidget(self.includeDigits)

        self.includeSymbols = QtWidgets.QCheckBox("Include Symbols")
        self.verticalLayout.addWidget(self.includeSymbols)

        # Cryptographically Secure Password Generator Section
        self.securePasswordLabel = QtWidgets.QLabel("Cryptographically Secure Password Generator")
        self.verticalLayout.addWidget(self.securePasswordLabel)

        self.secureLengthLabel = QtWidgets.QLabel("Length:")
        self.verticalLayout.addWidget(self.secureLengthLabel)
        self.secureLengthSpinBox = QtWidgets.QSpinBox()
        self.secureLengthSpinBox.setMinimum(6)
        self.secureLengthSpinBox.setMaximum(128)
        self.secureLengthSpinBox.setValue(16)
        self.verticalLayout.addWidget(self.secureLengthSpinBox)

        self.generateSecureButton = QtWidgets.QPushButton("Generate Secure Password")
        self.verticalLayout.addWidget(self.generateSecureButton)

        # Passphrase Generator Section
        self.passphraseLabel = QtWidgets.QLabel("Passphrase Generator")
        self.verticalLayout.addWidget(self.passphraseLabel)

        self.wordCountLabel = QtWidgets.QLabel("Number of Words:")
        self.verticalLayout.addWidget(self.wordCountLabel)
        self.wordCountSpinBox = QtWidgets.QSpinBox()
        self.wordCountSpinBox.setMinimum(3)
        self.wordCountSpinBox.setMaximum(12)
        self.wordCountSpinBox.setValue(4)
        self.verticalLayout.addWidget(self.wordCountSpinBox)

        self.generatePassphraseButton = QtWidgets.QPushButton("Generate Passphrase")
        self.verticalLayout.addWidget(self.generatePassphraseButton)

        # Password Generator with User Input Section
        self.userInputLabel = QtWidgets.QLabel("Password Generator with User Input")
        self.verticalLayout.addWidget(self.userInputLabel)

        self.userInputField = QtWidgets.QLineEdit()
        self.userInputField.setPlaceholderText("Enter your own input")
        self.verticalLayout.addWidget(self.userInputField)

        self.generateUserInputButton = QtWidgets.QPushButton("Generate Password from Input")
        self.verticalLayout.addWidget(self.generateUserInputButton)

        # Generate Button
        self.generateButton = QtWidgets.QPushButton("Generate Password")
        self.verticalLayout.addWidget(self.generateButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))

