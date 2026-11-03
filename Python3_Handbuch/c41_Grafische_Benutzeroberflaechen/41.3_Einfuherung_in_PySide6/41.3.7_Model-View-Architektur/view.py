from PySide6 import QtWidgets, QtGui, QtCore


class ViewDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.rahmen_stift = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.titel_text_stift = QtGui.QPen(QtGui.QColor(255,255,255)) 
        self.titel_farbe = QtGui.QBrush(QtGui.QColor(120,120,120)) 
        self.titel_farbe_aktiv = QtGui.QBrush(QtGui.QColor(0,0,120)) 
        self.hintergrund_farbe_aktiv = QtGui.QBrush(QtGui.QColor(230,230,255))
        self.text_stift = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.titel_schriftart = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold) 
        self.text_schriftart = QtGui.QFont("Helvetica", 10) 
        self.zeilen_hoehe = 15
        self.titel_hoehe = 20
        self.abstand = 4
        self.abstand_innen = 2
        self.abstand_text = 4

    def sizeHint(self, option, index):
        anz = len(index.data())
        return QtCore.QSize(170, self.zeilen_hoehe*anz + self.titel_hoehe)

    def paint(self, painter, option, index):
        rahmen = option.rect.adjusted(self.abstand, self.abstand, 
                                      -self.abstand, -self.abstand) 
        rahmen_titel = rahmen.adjusted(
            self.abstand_innen, self.abstand_innen, -self.abstand_innen+1, 0
        ) 
        rahmen_titel.setHeight(self.titel_hoehe) 
        rahmen_titel_text = rahmen_titel.adjusted(
            self.abstand_text, 0, self.abstand_text, 0
        ) 
        datensatz = index.data()
        painter.save()
        if option.state & QtWidgets.QStyle.State_Selected:
            painter.fillRect(rahmen, self.hintergrund_farbe_aktiv)
            painter.fillRect(rahmen_titel, self.titel_farbe_aktiv)
        else:
            painter.fillRect(rahmen_titel, self.titel_farbe)
        painter.setPen(self.rahmen_stift)
        painter.drawRect(rahmen) 
        # Titel schreiben
        painter.setPen(self.titel_text_stift) 
        painter.setFont(self.titel_schriftart) 
        painter.drawText(
            rahmen_titel_text, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
            datensatz[0]
        )
        # Adresse schreiben
        painter.setPen(self.text_stift) 
        painter.setFont(self.text_schriftart) 
        for i, eintrag in enumerate(datensatz[1:]): 
            painter.drawText(
                rahmen_titel.x() + self.abstand_text, 
                rahmen_titel.bottom() + (i+1)*self.zeilen_hoehe, 
                eintrag
            )
        painter.restore()
        
    def createEditor(self, parent, option, index):
        return QtWidgets.QTextEdit(parent)
            
    def setEditorData(self, editor, index):
        editor.setPlainText("\n".join(index.data()))

    def updateEditorGeometry(self, editor, option, index):
        rahmen = option.rect.adjusted(self.abstand, self.abstand, -self.abstand, -self.abstand) 
        editor.setGeometry(rahmen)
            
    def setModelData(self, editor, model, index):
        model.setData(index, editor.toPlainText().split("\n"))
            
    def eventFilter(self, editor, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            return False
        return QtWidgets.QItemDelegate.eventFilter(self, editor, event)


class View(QtWidgets.QListView):
   def __init__(self, modell, parent=None): 
       super().__init__(parent) 
       self.delegate = ViewDelegate()
       self.setItemDelegate(self.delegate) 
       self.setModel(modell)
       self.setVerticalScrollMode(QtWidgets.QListView.ScrollPerPixel)
