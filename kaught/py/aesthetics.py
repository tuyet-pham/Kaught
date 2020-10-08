#!/usr/bin/env python3
import tkinter as tk
from tkinter import Label, Entry
from tkinter import Frame, Button, Grid
from tkinter import TOP, LEFT, RIGHT, BOTTOM, Y, BOTH, END
from tkinter import TRUE, FALSE
from tkinter import Toplevel, Message
from tkinter import PanedWindow
from tkinter import Text, Scrollbar
from tkinter import PhotoImage

kaughtmsg = """
Hello user!

It's always good to stay organized and remain 
kaught up in your everyday agenda! I made Kaught so you don't have to :)
User registry is only to be stored within your own machine, so fret not. 
This program is open sourced so feel free to grab.
Let me know if any improvements can be made. 

@github.com/tuyet-pham
@tiidev19@gmail.com

"""


class KButtonLight(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'whitesmoke'
        self['fg'] = 'black'
        self['relief'] = 'flat'
        self['width'] = 30
        self['borderwidth'] = 0
        self['highlightthickness'] = 0
        self['activebackground'] = 'gray24'
        self['activeforeground'] = 'whitesmoke'

class KButtonDark(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'gray24'
        self['fg'] = 'white'
        self['relief'] = 'flat'
        self['width'] = 30
        self['borderwidth'] = 0
        self['highlightthickness'] = 0


class KLogo(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self.photo = PhotoImage(file="./public/kaught_logo200.png")
        self['image'] = self.photo


