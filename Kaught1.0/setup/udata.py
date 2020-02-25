#!usr/bin/env python3
import os
import sys
sys.path.append('../py')
from aesthetics import *

class Setup(tk.Frame):
    def __init__(self, master, width="500", height="600"):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.setupUser()

    def create_widgets(self):
        self.klogo = KLogo(self).pack(side=TOP,pady=20)

        self.kaughtM = Text(self, height=15, width=50, relief='flat')
        self.kaughtM.insert(tk.END, kaughtmsg)
        self.kaughtM.pack(side=TOP, fill=Y, pady=20)    

        self.exitButton = KButtonLight(self, text="Quit", command=quit).pack(side=RIGHT, pady=50,padx=2)
        self.nextButton = KButtonDark(self, text="Next", command=self.setupUser).pack(side=LEFT, pady=50, padx=2)        


    def setupUser(self):
        print("Hey")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kaught1.0 Setup")
    root.geometry("500x600")
    app = Setup(master=root)
    app.mainloop()
