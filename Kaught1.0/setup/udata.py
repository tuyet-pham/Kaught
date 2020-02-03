#!usr/bin/env python3
import os
import sys
sys.path.append('../py')
from aesthetics import *

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.pack()
        self.create_widgets()
        self.setupUser()

    def create_widgets(self):
        self.exitButton = KButtonLight(self, text="Quit").pack(side=LEFT)
        self.nextButton = KButtonDark(self, text="Next").pack(side=RIGHT)

    def setupUser(self):
        print("Hey")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kaught1.0 Setup")
    root.geometry("500x600")    
    app = Application(master=root)
    app.mainloop()
