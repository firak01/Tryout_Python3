#!/usr/bin/env python

import sys
from PySide6 import QtWidgets, QtCore
from hauptdialog import Ui_Hauptdialog


class MeinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Hauptdialog()
        self.ui.setupUi(self)

        # Slots einrichten
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonAbbrechen.clicked.connect(self.onAbbrechen)

    def onOK(self):
        # Daten auslesen
        print(f"Vorname: {self.ui.vorname.text()}")
        print(f"Nachname: {self.ui.nachname.text()}")
        print(f"Adresse: {self.ui.adresse.toPlainText()}")
        
        datum = self.ui.geburtsdatum.date().toString("dd.MM.yyyy")
        print(f"Geburtsdatum: {datum}")
        
        if self.ui.agb.checkState() == QtCore.Qt.Checked:
            print("AGBs akzeptiert")
        if self.ui.katalog.checkState() == QtCore.Qt.Checked:
            print("Katalog bestellt")
            
        self.close()

    def onAbbrechen(self):
        print("Schade")
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MeinDialog()
    dialog.show()
    sys.exit(app.exec())

