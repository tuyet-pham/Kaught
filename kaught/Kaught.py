#!usr/bin/env python3
import os
import sys
sys.path.append('./py')
from aesthetics import *

# ----------- Important switch class for ALL frames ----------- #
class Switch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.setdefault()
        self._frame = None

        self.menubar = Menu(self)
        self.about = Menu(self.menubar, tearoff=0,relief='flat')
        
       
        '''
            Add more to Menubar here, The key is a string 
            and the value would be a function call
        '''
        Menu_list = {'About': About, 'Kaught Main': EntryKaught}

        for k, v in Menu_list.items():
            self.add_to_menubar(1, k,v)

        self.about.add_command(label="Quit",command=quit )
        self.add_to_menubar(2, "Chose Color", None)

        
        self.menubar.add_cascade(label="Kaught", menu=self.about)
        self.config(menu=self.menubar)
        self.switch_frame(EntryKaught)

    def add_to_menubar(self, typeframe, item_label, frame_call):
        if typeframe == 1:
            self.about.add_command(label=item_label, command=lambda:self.switch_frame(frame_call))
        elif typeframe == 2:
            self.about.add_command(label=item_label, command=lambda:self.choose_color())
    
    def choose_color(self):
        frame = Toplevel(self)
        
        Change_color_list = {"Change background": 0,"Change button color":1, "Change accent":2}
        for k, v in Change_color_list.items():
            self.add_buttons(frame, 1, k, v)
        frame.grab_set()
    
    
    def add_buttons(self, frame, typebutton, k, v):
        if typebutton == 1:
            KButtonDark(frame, text = k, command=lambda:self.getcolor(v)).pack()
        elif typebutton == 2:
            KButtonLight(frame, text = k, command=lambda:self.getcolor(v)).pack()    
    
        
    def getcolor(self, att):
        if att == 0:
            self['bg'] = colorchooser.askcolor(title ="Choose color")[1]
        elif att == 1:
            self.menubar['bg'] = colorchooser.askcolor(title ="Choose color")[1]
        elif att == 2:
            self.about['bg'] = colorchooser.askcolor(title ="Choose color")[1]
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
    def setdefault(self):
        self.title("Kaught1.0 Setup")
        self.geometry("500x600")
        self['bg'] = 'snow1'
        
        


# ----------- Entry Page of App ----------- #
class EntryKaught(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        self.klogo = KLogo2(self, anchor="center", bg='snow1').pack(fill=tk.BOTH, expand=tk.FALSE)

        KButtonDark(self, anchor="center", text="Main Menu", command=lambda: master.switch_frame(MainMenu)).pack()
        KButtonLight(self, anchor="center", text="Quit", command=quit).pack(pady=10)

        


# ----------- Main Menu Apps ----------- #
class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        tk.Label(self, text="What to do now?", bg='snow1', font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=40)
        
        
        Button_frames = {"Calendar": Calendar, "Flash Cards": FlashCards,"Code Snippets": Snippets, "Send Text Messages": Message}
        for k, v in Button_frames.items():
            self.add_buttons(1, master,k,v)
            
        self.add_buttons(2, master, "Go to Kaught Main", EntryKaught)
        
    
    def add_buttons(self, typebutton, master, test_lable, frame_call):
        if typebutton == 1:
            KButtonDark(self, text=test_lable, command=lambda: master.switch_frame(frame_call)).pack(side=TOP, pady=5, fill=tk.X)
        elif typebutton == 2:
            KButtonLight(self, text=test_lable, command=lambda: master.switch_frame(frame_call)).pack(side=TOP, pady=5, fill=tk.X)



# ----------- About App ----------- #
class About(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        self.klogo = KLogo(self, bg='snow1').pack(side=TOP,pady=20)

        self.kaughtM = Text(self, height=15, width=53, relief='flat')
        self.kaughtM.insert(tk.END, kaughtmsg)
        self.kaughtM.config(state='disabled')
        self.kaughtM.pack(side=TOP, fill=Y, pady=20)
        
        KButtonDark(self, text="Back", bg='snow1', command=lambda: master.switch_frame(EntryKaught)).pack(side=RIGHT, pady=20, padx=2)
        



# ----------- About App ----------- #
class FlashCards(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        tk.Label(self, text="FlashCards", bg='snow1', font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=5)
        
        KButtonDark(self, text="Back", bg='snow1', command=lambda: master.switch_frame(MainMenu)).pack(side=RIGHT, pady=20, padx=2)



# ----------- About App ----------- #
class Message(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        tk.Label(self, text="Message", bg='snow1', font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=5)
        KButtonDark(self, text="Back", bg='snow1', command=lambda: master.switch_frame(MainMenu)).pack(side=RIGHT, pady=20, padx=2)
        


# ----------- About App ----------- #
class Snippets(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        tk.Label(self, text="Snippets", bg='snow1', font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=5)
        KButtonDark(self, text="Back", bg='snow1', command=lambda: master.switch_frame(MainMenu)).pack(side=RIGHT, pady=20, padx=2)



# ----------- About App ----------- #
class Calendar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self['bg'] = 'snow1'
        tk.Label(self, text="Calendar", bg='snow1', font=('Helvetica', 18, "bold")).pack(side=TOP, fill="x", pady=5)
        KButtonDark(self, text="Back", bg='snow1', command=lambda: master.switch_frame(MainMenu)).pack(side=RIGHT, pady=20, padx=2)



if __name__ == "__main__":
    app = Switch()
    app.mainloop()
