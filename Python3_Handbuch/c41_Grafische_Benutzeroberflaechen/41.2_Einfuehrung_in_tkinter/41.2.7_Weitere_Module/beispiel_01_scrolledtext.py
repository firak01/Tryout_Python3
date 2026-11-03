#!/usr/bin/env python

import tkinter
import tkinter.scrolledtext


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.scrolledtext.ScrolledText(master)
        self.text.pack()
        self.text.insert("end", """Im Abschnitt über das Text-Widget haben wir gesagt, dass es über die Option yscrollcommand möglich ist, ein Text-Widget mit einer vertikalen Scrollbar auszustatten. Da aber eine solche vertikale Scrollbar häufig erwünscht ist, wäre es umständlich, jedes Mal den Code zum Instanziieren und Anbinden der Scrollbar schreiben zu müssen.
Für diesen Zweck existiert das Modul scrolledtext im Paket tkinter, das das Widget ScrolledText bereitstellt. Dieses Widget verhält sich wie ein Text-Widget, ist aber standardmäßig mit einer vertikalen Scrollbar ausgestattet, sodass sich der Programmierer um diese nicht mehr zu kümmern braucht.""")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
