#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import *
from tkinter import filedialog
from excel_to_sql_script import ExcelToSql


class ExcelToSqlPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.sql_path = Entry(self)
        self.excel_path = Entry(self)
        self.config(bg="yellow")
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=60)

        Label(self, text="待转换的excel").grid(row=0, column=0, pady=10, sticky=tkinter.W)
        self.excel_path.grid(row=1, column=0, sticky=tkinter.EW)
        Button(self, text="选择", command=self.get_excel_path).grid(row=1, column=1, sticky=tkinter.W)

        Label(self, text="sql模型文件夹").grid(row=2, column=0, pady=10, sticky=tkinter.W)
        self.sql_path.grid(row=3, column=0, sticky=tkinter.EW)
        Button(self, text="选择", command=self.get_sql_path).grid(row=3, column=1, sticky=tkinter.W)

        Button(self, text="转换", command=self.merge_action, width=10).grid(row=4, columnspan=2, pady=20)

    def get_excel_path(self):
        path = filedialog.askopenfilename(title='选择excel')
        self.excel_path.delete(0, "end")
        self.excel_path.insert(0, path)

    def get_sql_path(self):
        path = filedialog.askdirectory(title='选择文件夹')
        self.sql_path.delete(0, "end")
        self.sql_path.insert(0, path)

    def merge_action(self):
        script = ExcelToSql(self.excel_path.get(), self.sql_path.get())
        script.run()
