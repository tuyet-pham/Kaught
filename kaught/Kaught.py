#!usr/bin/env python3
import os
import sys
sys.path.append('./py')
from aesthetics import *
from tkinter import PhotoImage, Menu

# ----------- Important switch class for ALL frames ----------- #
class Switch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kaught1.0 Setup")
        self.geometry("550x600")
        self._frame = None

        menubar = Menu(self)
        about = Menu(menubar, tearoff=0)
        about.add_command(label="About", command=lambda :self.switch_frame(About))
        about.add_command(label="Quit", command=quit)

        menubar.add_cascade(label="Kaught", menu=about)
        self.config(menu=menubar)
        self.switch_frame(EntryKaught)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# ----------- Front Page of App ----------- #
class EntryKaught(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.klogo = KLogo(self).pack(side=TOP,pady=20)
        
        KButtonDark(self, text="Main Menu", command=lambda: master.switch_frame(MainMenu)).pack(side=BOTTOM, pady=50)
        


# ----------- Main Menu Apps ----------- #
class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="What to do now?", font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=5)
        
        KButtonDark(self, text="Flash Cards", command=lambda: master.switch_frame(EntryKaught)).pack(side=TOP, pady=5, fill=tk.X, expand=FALSE)
        KButtonDark(self, text="Code Snippets", command=lambda: master.switch_frame(EntryKaught)).pack(side=TOP, pady=5, fill=tk.X)
        KButtonDark(self, text="Code Snippets", command=lambda: master.switch_frame(EntryKaught)).pack(side=TOP, pady=5, fill=tk.X)
        KButtonLight(self, text="Back", command=lambda: master.switch_frame(EntryKaught)).pack(side=TOP, pady=5, fill=tk.X)



# ----------- About App ----------- #
class About(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.klogo = KLogo(self).pack(side=TOP,pady=20)

        self.kaughtM = Text(self, height=15, width=53, relief='flat')
        self.kaughtM.insert(tk.END, kaughtmsg)
        self.kaughtM.config(state='disabled')
        self.kaughtM.pack(side=TOP, fill=Y, pady=20)
        
        KButtonDark(self, text="Back", command=lambda: master.switch_frame(EntryKaught)).pack(side=RIGHT, pady=20, padx=2)




if __name__ == "__main__":
    app = Switch()
    app.mainloop()
