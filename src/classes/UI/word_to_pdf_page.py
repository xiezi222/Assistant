#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import Frame, Label, Button, Entry, filedialog
from src.classes.script.word_to_pdf import WordToPDF


class WordToPDFPage(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.sql_path = Entry(self)
        self.word_path = Entry(self)
        self.root = master
        self.add_subviews()

    def add_subviews(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=60)

        Label(self, text="待转换的word").grid(row=0, column=0, pady=10, sticky='w')
        self.word_path.grid(row=1, column=0, padx=(0, 10), sticky='ew')
        Button(self, text="选择", command=self.get_word_path).grid(row=1, column=1, sticky='w')
        Button(self, text="转换", command=self.merge_action, width=10).grid(row=4, columnspan=2, pady=20)

    def get_word_path(self):
        path = filedialog.askopenfilename(title='选择word')
        self.word_path.delete(0, "end")
        self.word_path.insert(0, path)

    def merge_action(self):
        script = WordToPDF(self.word_path.get())
        script.run()
