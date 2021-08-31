#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
from tkinter import filedialog


class MergePage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.path = Entry(self)
        self.config(bg="yellow")
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=60)

        Label(self, text="待合并的excel所在文件夹").grid(row=0, column=0, pady=10, sticky=tkinter.W)
        self.path.grid(row=1, column=0, sticky=tkinter.EW)
        Button(self, text="选择", command=self.get_path).grid(row=1, column=1, sticky=tkinter.W)
        Button(self, text="合并", command=self.merge_action, width=10).grid(row=2, columnspan=2, pady=20)

    def get_path(self):
        path = filedialog.askdirectory(title='选择文件夹')
        self.path.delete(0, "end")
        self.path.insert(0, path)

    def merge_action(self):
        path = self.path.get()
        print(path)
