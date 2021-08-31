#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
from tkinter import filedialog
from merge_page import MergePage
from excel_to_sql_page import ExcelToSqlPage


class MainPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.config(bg="green")
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        list_view = Frame(self, bg="purple")
        list_view.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.contentView = Frame(self, bg="red")
        self.contentView.grid(row=0, column=1, sticky=tkinter.NSEW)

        Button(list_view, text="合并excel文件", command=self.merge_action).pack(pady=10)
        Button(list_view, text="提取列名首字母", command=self.pinyin_action).pack(pady=10)
        Button(list_view, text="excel转sql", command=self.transform_action).pack(pady=10)
        self.merge_action()

    def merge_action(self):
        pages = self.contentView.pack_slaves()
        for page in pages:
            page.destroy()
        MergePage(self.contentView).pack(fill=tkinter.BOTH, expand=True)

    def pinyin_action(self):
        print("pinyin_action")

    def transform_action(self):
        pages = self.contentView.pack_slaves()
        for page in pages:
            page.destroy()
        ExcelToSqlPage(self.contentView).pack(fill=tkinter.BOTH, expand=True)
