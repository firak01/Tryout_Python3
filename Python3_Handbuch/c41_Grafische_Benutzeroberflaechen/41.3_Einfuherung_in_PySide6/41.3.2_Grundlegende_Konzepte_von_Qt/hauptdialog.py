# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hauptdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Hauptdialog(object):
    def setupUi(self, Hauptdialog):
        if not Hauptdialog.objectName():
            Hauptdialog.setObjectName(u"Hauptdialog")
        Hauptdialog.resize(331, 399)
        self.verticalLayout = QVBoxLayout(Hauptdialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Hauptdialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.vorname = QLineEdit(self.groupBox)
        self.vorname.setObjectName(u"vorname")

        self.gridLayout.addWidget(self.vorname, 0, 1, 1, 1)

        self.nachname = QLineEdit(self.groupBox)
        self.nachname.setObjectName(u"nachname")

        self.gridLayout.addWidget(self.nachname, 1, 1, 2, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.geburtsdatum = QDateEdit(self.groupBox)
        self.geburtsdatum.setObjectName(u"geburtsdatum")

        self.horizontalLayout_2.addWidget(self.geburtsdatum)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.adresse = QTextEdit(self.groupBox)
        self.adresse.setObjectName(u"adresse")

        self.gridLayout.addWidget(self.adresse, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Hauptdialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.agb = QCheckBox(self.groupBox_2)
        self.agb.setObjectName(u"agb")

        self.verticalLayout_2.addWidget(self.agb)

        self.katalog = QCheckBox(self.groupBox_2)
        self.katalog.setObjectName(u"katalog")

        self.verticalLayout_2.addWidget(self.katalog)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonOK = QPushButton(Hauptdialog)
        self.buttonOK.setObjectName(u"buttonOK")

        self.horizontalLayout.addWidget(self.buttonOK)

        self.buttonAbbrechen = QPushButton(Hauptdialog)
        self.buttonAbbrechen.setObjectName(u"buttonAbbrechen")

        self.horizontalLayout.addWidget(self.buttonAbbrechen)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Hauptdialog)

        self.buttonOK.setDefault(True)


        QMetaObject.connectSlotsByName(Hauptdialog)
    # setupUi

    def retranslateUi(self, Hauptdialog):
        Hauptdialog.setWindowTitle(QCoreApplication.translate("Hauptdialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptdialog", u"Pers\u00f6nliche Daten", None))
        self.label.setText(QCoreApplication.translate("Hauptdialog", u"Vorname", None))
        self.label_2.setText(QCoreApplication.translate("Hauptdialog", u"Nachname", None))
        self.label_3.setText(QCoreApplication.translate("Hauptdialog", u"Geburtsdatum", None))
        self.label_4.setText(QCoreApplication.translate("Hauptdialog", u"Adresse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Hauptdialog", u"Weitere Angaben", None))
        self.agb.setText(QCoreApplication.translate("Hauptdialog", u"AGBs gelesen und akzeptiert", None))
        self.katalog.setText(QCoreApplication.translate("Hauptdialog", u"Katalog bestellen", None))
        self.buttonOK.setText(QCoreApplication.translate("Hauptdialog", u"OK", None))
        self.buttonAbbrechen.setText(QCoreApplication.translate("Hauptdialog", u"Abbrechen", None))
    # retranslateUi

