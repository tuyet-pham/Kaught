#!/usr/bin/env python3
import os
import sys
sys.path.append('./py')
from kui import *

# ----------- Important switch class for ALL frames ----------- #
class Switch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.setdefault()
        self._frame = None
        self.switch_frame(EntryMenu)
    

    def switch_frame(self, frame_class):
        if(frame_class == EntryMenu):
            self.buttonnav.pack_forget()
        else:
            self.buttonnav.pack(side=LEFT, fill=BOTH)
            
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side=RIGHT, fill=BOTH, expand=TRUE)
 
    
    def setdefault(self):
        self.title("Stock Prediction")
        self.geometry("1200x900")
        self['bg'] = 'gray13'
        self.buttonnav = ButtonBar(self)
        

    def reset(self):
        frame = Toplevel(self, width=100, height=50)
        frame['bg'] = self['bg']
        KLabel(frame, text="Reset").pack(side=TOP, fill="x", pady=10, padx=20)
        frame.grab_set()
        
        
        
class ButtonBar(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.rowat = 0
        self['bg'] = 'gray27'
        
        Button_frames = {"Main": MainMenu, "Update Files": FilePicker, "View Calendar": Calendar, "Flash Cards": FlashCards, "To-Dos": ToDo}
        for k, v in Button_frames.items():
            self.add_buttons(1, master, k, v)
            
        self.add_buttons(2, master, test_lable="Quit", frame_call=quit)

    
    def add_buttons(self, typebutton, master, test_lable, frame_call):
        if typebutton == 1:
            KButtonDark(self, text=test_lable, command=lambda: master.switch_frame(frame_call)).grid(row=self.rowat, sticky=W+N+S)
            self.rowat = self.rowat+1
        elif typebutton == 2:
            KButtonDark(self, text=test_lable, bg='MediumSlateBlue', fg='snow', height=3, command=frame_call).grid(row=self.rowat, sticky=W+N+S)
            self.rowat = self.rowat+1
        



# ----------- Entry Page of App ----------- #
class EntryMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="Get kaught up!").pack(fill=BOTH, expand=TRUE)
        KButtonDark(self, width=20, text="Enter", bg='MediumSlateBlue', fg='snow', height=2, command=lambda: master.switch_frame(MainMenu)).pack(side=BOTTOM, pady=50, padx=50, anchor='se')



# ----------- Main Menu Apps ----------- #
class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="Kaught News\nand Update").pack(side=TOP, fill="x", pady=10)
        KButtonDark(self, width=20, text="Close", bg='MediumSlateBlue', fg='snow', height=2, command=lambda: master.switch_frame(EntryMenu)).pack(side=TOP, pady=10)
       
        

# ----------- About App ----------- #
class FilePicker(Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        self.filename=""
        KLabel(self, fg='gray70', text="Choose Sets").grid(row=0, column=0, columnspan=4, pady=15, padx=15, sticky=W)

        self.setdefault()
        self.setrequired_(2)

    
    def chosefile(self, stype):
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file 
        if stype == 1:
            self.entrytrain.delete(0,'end')
            self.entrytrain.insert(0, self.filename)
        elif stype == 2:
            self.entrydev.delete(0,'end')
            self.entrydev.insert(0, self.filename)
        elif stype == 3:
            self.entryfull.delete(0,'end')
            self.entryfull.insert(0, self.filename)
        elif stype == 4:
            self.entrytest.delete(0,'end')
            self.entrytest.insert(0, self.filename)
        
    def setrequired_(self, stype):
        if stype == 2:
            self.entrydev.delete(0,'end')
            self.entrytrain.delete(0,'end')
            self.browsebut1['state'] = tk.DISABLED
            self.browsebut2['state'] = tk.DISABLED
            self.entrydev['state'] = tk.DISABLED
            self.entrytrain['state'] = tk.DISABLED
            self.browsebut3['state'] = tk.NORMAL
            self.entryfull['state'] = tk.NORMAL
        elif stype == 1:
            self.browsebut1['state'] = tk.NORMAL
            self.browsebut2['state'] = tk.NORMAL
            self.entrydev['state'] = tk.NORMAL
            self.entrytrain['state'] = tk.NORMAL
            self.browsebut3['state'] = tk.DISABLED
            self.entryfull.delete(0,'end')
            self.entryfull['state'] = tk.DISABLED
    
    def runstock(self):
        if self.entryfull['state'] == tk.DISABLED:
            trainfile = self.entrytrain.get()
            devfile = self.entrydev.get()
            testfile = self.entrytest.get()
            print(trainfile)
            print(devfile)
            print(testfile)
        elif self.entryfull['state'] == tk.NORMAL:
            fullpath = self.entryfull.get()
            testfile = self.entrytest.get()
            print(fullpath)
            print(testfile)
            

    def setdefault(self):
        KLabel(self, font=('Helvetica', 11, "normal"), text="Does your set require splitting?").grid(row=1, column=0, columnspan=3, padx=15, sticky=W)

        v = tk.IntVar()
        KRadiobutton(self, text="Splitting required", command=lambda: self.setrequired_(2), variable=v, value=1).grid(row=2, column=0, columnspan=2, pady=5, padx=15, sticky=W)
        KRadiobutton(self, text="Splitting not required", variable=v, value=2, command=lambda: self.setrequired_(1)).grid(row=2, column=2, columnspan=4, pady=5, sticky=W)
        
        KLabel(self, font=('Helvetica', 11, "normal"), text="Training set").grid(row=3, column=0, columnspan=2, padx=15, sticky=W)
        self.browsebut1 = KButtonDark(self, width=15, text="Browse", bg='MediumSlateBlue', fg='snow', height=1, command=lambda: self.chosefile(1))
        self.browsebut1.grid(row=4, column=2, columnspan=4, pady=5, sticky=E)
        self.entrytrain = KEntry(self, width=45)
        self.entrytrain.grid(row=4, column=0, ipady=3, columnspan=2, pady=5, padx=15, sticky=W)
        
        KLabel(self, font=('Helvetica', 11, "normal"), text="Developement set").grid(row=5, column=0, columnspan=2, padx=15, sticky=W)
        self.browsebut2 = KButtonDark(self, width=15, text="Browse", bg='MediumSlateBlue', fg='snow', height=1, command=lambda: self.chosefile(2))
        self.browsebut2.grid(row=6, column=2, columnspan=4, pady=5, sticky=E)
        self.entrydev = KEntry(self, width=45)
        self.entrydev.grid(row=6, column=0, ipady=3, columnspan=2, pady=5, padx=15, sticky=W)
        
        KLabel(self, font=('Helvetica', 11, "normal"), text="Full Set").grid(row=7, column=0, columnspan=2, padx=15, sticky=W)
        self.browsebut3 = KButtonDark(self, width=15, text="Browse", bg='MediumSlateBlue', fg='snow', height=1, command=lambda: self.chosefile(3))
        self.browsebut3.grid(row=8, column=2, columnspan=4, pady=5, sticky=E)
        self.entryfull = KEntry(self, width=45)
        self.entryfull.grid(row=8, column=0, ipady=3, columnspan=2, pady=5, padx=15, sticky=W)
        
        KLabel(self, font=('Helvetica', 11, "normal"), text="Testing Set").grid(row=9, column=0, columnspan=2, padx=15, sticky=W)
        self.browsebut4 = KButtonDark(self, width=15, text="Browse", bg='MediumSlateBlue', fg='snow', height=1, command=lambda: self.chosefile(4))
        self.browsebut4.grid(row=10, column=2, columnspan=4, pady=5, sticky=E)
        self.entrytest = KEntry(self, width=45)
        self.entrytest.grid(row=10, column=0, ipady=3, columnspan=2, pady=5, padx=15, sticky=W)
        
        
        
        self.runbutton = KButtonDark(self,width=15, text="Select Sets", bg='MediumSlateBlue', fg='snow', height=2, command=lambda: self.runstock())
        self.runbutton.grid(row=11, column=0, columnspan=4, pady=10, padx=15, sticky=W)


 
# ----------- About App ----------- #
class About(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']

        self.KaughtM = Text(self, height=15, width=53, relief='flat')
        self.KaughtM.config(state='disabled')
        self.KaughtM.pack(side=TOP, fill=Y, pady=20)
        
        

# ----------- About App ----------- #
class FlashCards(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="FlashCards").pack(side=TOP, fill="x", pady=10)
        
        
# ----------- About App ----------- #
class ToDo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="To-Do").pack(side=TOP, fill="x", pady=10)



# ----------- About App ----------- #
class Calendar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="Calendar").pack(side=TOP, fill="x", pady=10)


# ----------- About App ----------- #
class Notes(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="Notes").pack(side=TOP, fill="x", pady=10)


# ----------- About App ----------- #
class Snippets(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = master['bg']
        KLabel(self, text="Calendar").pack(side=TOP, fill="x", pady=10)



if __name__ == "__main__":
    app = Switch()
    app.mainloop()
    