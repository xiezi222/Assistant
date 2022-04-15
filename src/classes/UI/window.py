#!/usr/bin/python3
# -*- coding: UTF-8 -*-

try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk
from main_page import MainPage


class Window:

    def __init__(self):
        self.init_window()

    def init_window(self):
        window = Tk()
        self.setup_window(window)
        self.create_main_view(window)
        window.mainloop()

    def setup_window(self, window):
        window.title("爱妻工作小助手")
        width = 480
        height = 320
        left = int(window.winfo_screenwidth() / 2 - width / 2)
        top = int(window.winfo_screenheight() / 2 - height / 2)
        window.geometry(f"{width}x{height}+{left}+{top}")

    def create_main_view(self, window):
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
        MainPage(window).grid(sticky='nsew')
