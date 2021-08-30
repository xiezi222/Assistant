#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import *
from tkinter import filedialog


class ExcelToSqlPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg="pink")
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        merge = self.create_button("选择excel文件", self.merge_action)

        pinyin = self.create_button("选择sql语句模型文件夹", self.pinyin_action)
        transform = self.create_button("转换", self.transform_action)

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



    def openfile(self):
        sfname = filedialog.askopenfilename(title='选择Excel文件', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
        print(sfname)
        return sfname
