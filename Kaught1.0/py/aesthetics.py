#!/usr/bin/env python3
import tkinter as tk
from tkinter import Label, Entry
from tkinter import Frame, Button
from tkinter import TOP, LEFT, RIGHT, BOTTOM, RIGHT
from tkinter import TRUE, FALSE
from tkinter import Toplevel, Message
from tkinter import PanedWindow
from tkinter import PhotoImage


class KButtonLight(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'whitesmoke'
        self['fg'] = 'black'
        self['relief'] = 'flat'
        self['width'] = 10
        self['borderwidth'] = 0
        self['highlightthickness'] = 0
        self['pady'] = 5
        self['activebackground'] = 'gray24'
        self['activeforeground'] = 'whitesmoke'

class KButtonDark(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'gray24'
        self['fg'] = 'white'
        self['relief'] = 'flat'
        self['width'] = 10
        self['borderwidth'] = 0
        self['highlightthickness'] = 0
        self['pady'] = 5


class KLogo(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self["photo"] = PhotoImage(file="kaught_logo300.png")
        self["image"] = photo
        self["pady"] = 5
        self["padx"] = 5