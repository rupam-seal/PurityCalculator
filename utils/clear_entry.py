from tkinter import *

class ClearEntry():
    def __init__(self, obj):
        self.obj = obj

    # clear all the entry after complete the task
    def clear(self):
        self.obj.entry0.delete(0, END)
        self.obj.entry1.delete(0, END)
        self.obj.entry2.delete(0, END)
        self.obj.entry3.delete(0, END)
        self.obj.entry4.delete(0, END)
        self.obj.entry5.delete(0, END)
        self.obj.entry6.delete(0, END)
