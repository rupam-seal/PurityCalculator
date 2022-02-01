from tkinter import *
from tkinter import filedialog

from calc import Calculate
from utils.insert_default_value import InsertDefault


'''
    Gui class: [all the tkinter entry and buttons]
'''
class Gui():
    def __init__(self):
        # window
        self.window = Tk()

        self.window.geometry("479x580")
        self.window.configure(bg = "#ffffff")
        self.window.iconbitmap("assets/Logo.ico")
        self.window.title("Card Printing Designer")

        # canvas and background
        self.background()

        # tkinter entry
        self.entry()

        # tkinter button
        self.button()

        # inserting default value to the entry
        InsertDefault(self).insert_default_value_to_entry()

    # inserting background to the window
    def background(self):
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 580,
            width = 479,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"assets/background.png")
        self.background = self.canvas.create_image(
            295.0, 265.0,
            image=self.background_img)

    # Entry method
    def entry(self):
        self.entry0_img = PhotoImage(file = f"assets/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            132.0, 175.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry0.place(
            x = 42.0, y = 158,
            width = 180.0,
            height = 32)

        self.entry1_img = PhotoImage(file = f"assets/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            347.0, 175.0,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry1.place(
            x = 257.0, y = 158,
            width = 180.0,
            height = 32)

        self.entry2_img = PhotoImage(file = f"assets/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            132.0, 255.0,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry2.place(
            x = 42.0, y = 238,
            width = 180.0,
            height = 32)

        self.entry3_img = PhotoImage(file = f"assets/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            347.0, 255.0,
            image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry3.place(
            x = 257.0, y = 238,
            width = 180.0,
            height = 32)

        self.entry4_img = PhotoImage(file = f"assets/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            132.0, 335.0,
            image = self.entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry4.place(
            x = 42.0, y = 318,
            width = 180.0,
            height = 32)

        self.entry5_img = PhotoImage(file = f"assets/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            347.0, 335.0,
            image = self.entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry5.place(
            x = 257.0, y = 318,
            width = 180.0,
            height = 32)

        self.entry6_img = PhotoImage(file = f"assets/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            132.0, 415.0,
            image = self.entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry6.place(
            x = 42.0, y = 398,
            width = 180.0,
            height = 32)

        self.entry7_img = PhotoImage(file = f"assets/img_textBox7.png")
        self.entry7_bg = self.canvas.create_image(
            347.0, 415.0,
            image = self.entry7_img)

        self.entry7 = Entry(
            bd = 0,
            bg = "#ededed",
            highlightthickness = 0)

        self.entry7.place(
            x = 257.0, y = 398,
            width = 180.0,
            height = 32)

    # Button method
    def button(self):
        self.img0 = PhotoImage(file = f"assets/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("b0"),
            relief = "flat")

        self.b0.place(
            x = 247, y = 497,
            width = 200,
            height = 34)

        self.img1 = PhotoImage(file = f"assets/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.purity_result(self),
            relief = "flat")

        self.b1.place(
            x = 32, y = 497,
            width = 200,
            height = 34)

        self.img2 = PhotoImage(file = f"assets/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("b2"),
            relief = "flat")

        self.b2.place(
            x = 416, y = 45,
            width = 31,
            height = 14)

        self.img3 = PhotoImage(file = f"assets/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.open_excel_sheet(self),
            relief = "flat")

        self.b3.place(
            x = 101, y = 134,
            width = 18,
            height = 17)

        self.img4 = PhotoImage(file = f"assets/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: ButtonCommand.select_saved_location(self),
            relief = "flat")

        self.b4.place(
            x = 311, y = 134,
            width = 18,
            height = 17)



'''
    ButtonCommand: [all the onClick function of tkinter buttons]
'''
class ButtonCommand(Gui):
    def open_excel_sheet(self):
        path = filedialog.askopenfilename()
        self.entry0.insert(END, path)
        print(path)

    def select_saved_location(self):
        path = filedialog.askdirectory()
        self.entry1.insert(END, path)
        print(path)

    def purity_result(self):
        calculate_p = Calculate(self)
        calculate_p.calculate_purity()

    # def print_hard_copy(self):
    #     print_copy = Calculate(self)
    #     print_copy.print_excel_sheet_hard_copy()