#!/usr/bin/python3
# -*- coding: UTF-8 -*-

try:
    from Tkinter import Frame, Button
    from Tkinter.ttk import Separator
except ImportError:
    from tkinter import Frame, Button
    from tkinter.ttk import Separator
from merge_page import MergePage
from excel_to_sql_page import ExcelToSqlPage
from word_to_pdf_page import WordToPDFPage


class MainPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        list_view = Frame(self)
        list_view.grid(row=0, column=0, sticky='nsew')

        Separator(self, orient='horizontal').grid(row=0, column=1, sticky='ns')
        self.contentView = Frame(self)
        self.contentView.grid(row=0, column=2, sticky='nsew')

        Button(list_view, text="合并excel文件", command=self.merge_action).pack(pady=10)
        Button(list_view, text="提取列名首字母", command=self.pinyin_action).pack(pady=10)
        Button(list_view, text="excel转sql", command=self.transform_action).pack(pady=10)
        Button(list_view, text="word_to_pdf", command=self.word_to_pdf_action).pack(pady=10)
        self.merge_action()

    def merge_action(self):
        pages = self.contentView.pack_slaves()
        for page in pages:
            page.destroy()
        MergePage(self.contentView).pack(fill='both', expand=True)

    def pinyin_action(self):
        print("pinyin_action")

    def transform_action(self):
        pages = self.contentView.pack_slaves()
        for page in pages:
            page.destroy()
        ExcelToSqlPage(self.contentView).pack(fill='both', expand=True)

    def word_to_pdf_action(self):
        pages = self.contentView.pack_slaves()
        for page in pages:
            page.destroy()
        WordToPDFPage(self.contentView).pack(fill='both', expand=True)
