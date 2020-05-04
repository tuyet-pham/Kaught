#!usr/bin/env python3
import os
import sys
sys.path.append('../py')
from aesthetics import *
from tkinter import PhotoImage

class Switch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kaught1.0 Setup")
        self.geometry("500x600")
        self._frame = None
        self.switch_frame(Setup)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Setup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.klogo = KLogo(self).pack(side=TOP,pady=20)

        self.kaughtM = Text(self, height=15, width=50, relief='flat')
        self.kaughtM.insert(tk.END, kaughtmsg)
        self.kaughtM.pack(side=TOP, fill=Y, pady=20)    
        
        KButtonDark(self, text="Next", command=lambda: master.switch_frame(Userinfo)).pack(side=LEFT, pady=50, padx=2)
        KButtonLight(self, text="Quit", command=quit).pack(side=RIGHT, pady=50,padx=2)


class Userinfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="User info", font=('Helvetica', 20)).pack(side="top", fill="x", pady=10)

        Label(self, text="Username").pack(side=LEFT, pady=10, padx=10)
        self.username = Entry(self, bd=0, relief='flat', selectborderwidth=0).pack(side=RIGHT, pady=10, padx=10)
        
        Label(self, text="Password").pack(side=LEFT, pady=10, padx=10)
        self.password = Entry(self, bd=0, relief='flat', selectborderwidth=0).pack(side=RIGHT, pady=10, padx=10)
        
        KButtonDark(self, text="Next", command=lambda: master.switch_frame(FinishUser)).pack(side=LEFT, pady=50, padx=2)
        KButtonLight(self, text="Quit", command=quit).pack(side=RIGHT, pady=50,padx=2)
        KButtonLight(self, text="Back", command=lambda: master.switch_frame(Setup)).pack(side=RIGHT, pady=50,padx=2)


class FinishUser(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Finish User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        KButtonDark(self, text="Finish!", command=quit).pack(side=LEFT, pady=50, padx=2)
        KButtonLight(self, text="Quit", command=quit).pack(side=RIGHT, pady=50,padx=2)
        KButtonLight(self, text="Back", command=lambda: master.switch_frame(Userinfo)).pack(side=RIGHT, pady=50,padx=2)




if __name__ == "__main__":    
    app = Switch()
    app.mainloop()
