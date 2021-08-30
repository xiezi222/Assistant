#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import mainPage


class Window:

    def __init__(self):
        self.init_window()

    def init_window(self):
        window = tkinter.Tk()
        self.setup_window(window)
        self.create_menu(window)
        self.create_main_view(window)
        window.mainloop()

    def setup_window(self, window):
        window.title("爱妻工作小助手")
        width = 200
        height = 300
        left = int(window.winfo_screenwidth() / 2 - width / 2)
        top = int(window.winfo_screenheight() / 2 - height / 2)
        window.geometry(f"{width}x{height}+{left}+{top}")

    def create_menu(self, window):
        pass

    def create_main_view(self, window):
        self.root_view = mainPage.MainPage(window)
        self.root_view.pack(expand=True, fill=tkinter.BOTH)