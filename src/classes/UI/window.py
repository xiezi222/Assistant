#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from ctypes import windll
from tkinter import Tk
from src.classes.UI.main_page import MainPage

class Window:

    def __init__(self):
        self.init_window()

    def init_window(self):
        window = Tk()
        # 调用api设置成由应用程序缩放
        windll.shcore.SetProcessDpiAwareness(1)
        # 调用api获得当前的缩放因子
        ScaleFactor = windll.shcore.GetScaleFactorForDevice(0)
        # 设置缩放因子 一个点是1/72英寸
        window.tk.call('tk', 'scaling', ScaleFactor / 72)
        self.setup_window(window)
        self.create_main_view(window)
        window.mainloop()

    def setup_window(self, window):
        window.title("爱妻工作小助手")
        width = 900
        height = 600
        left = int(window.winfo_screenwidth() / 2 - width / 2)
        top = int(window.winfo_screenheight() / 2 - height / 2)
        window.geometry(f"{width}x{height}+{left}+{top}")

    def create_main_view(self, window):
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
        MainPage(window).grid(sticky='nsew')
