#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack()

    self.s1 = tkinter.Spinbox(self)
    self.s1["from"] = 0
    self.s1["to"] = 100
    self.s1.pack()


if __name__ == "__main__":
  root = tkinter.Tk()
  root.geometry("150x30")
  app = MyApp(root)
  app.mainloop()
