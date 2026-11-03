#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack(padx=5, pady=5)
        
        self.name = tkinter.StringVar()
        self.name.set("Ihr Name...")
        self.nameEntry["textvariable"] = self.name
        
        self.ok = tkinter.Button(self)
        self.ok["text"] = "Ok"
        self.ok["command"] = self.quit
        self.ok.pack(side="right", padx=5, pady=5)
        
        self.rev = tkinter.Button(self)
        self.rev["text"] = "Umdrehen"
        self.rev["command"] = self.onReverse
        self.rev.pack(side="right", padx=5, pady=5)

    def onReverse(self):
        self.name.set(self.name.get()[::-1])


if __name__ == "__main__":
    root = tkinter.Tk()
#    root.geometry("150x50")
    app = MyApp(root)
    app.mainloop()
