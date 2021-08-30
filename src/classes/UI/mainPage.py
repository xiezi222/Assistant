#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import excelToSqlPage
from tkinter import *
from tkinter import filedialog


class MainPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg="pink")
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        merge = self.create_button("合并excel文件", self.merge_action)
        pinyin = self.create_button("提取列名首字母", self.pinyin_action)
        transform = self.create_button("excel转sql", self.transform_action)

    def create_button(self, text, action):
        button = Button(self, text=text, command=action, bg="red", width=20, height=3)
        button.pack()
        return button

    def merge_action(self):
        self.openfile()

    def pinyin_action(self):
        print("pinyin_action")

    def transform_action(self):
        print("transform_action")
        self.transform_page = excelToSqlPage.ExcelToSqlPage(self.root)
        self.destroy()
        self.transform_page.pack()


    def openfile(self):
        sfname = filedialog.askopenfilename(title='选择Excel文件', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        print(sfname)
        return sfname
