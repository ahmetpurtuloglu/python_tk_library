import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import database_lib
import langpack
from centerscreen import center_screen_geometry


class AddBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.database_lib = database_lib.LibraryManager()
        self.parent = parent
        self.i18n = parent.i18n
        self.geometry(center_screen_geometry(screen_width=parent.win.winfo_screenwidth(),
                                    screen_height=parent.win.winfo_screenheight(),
                                    window_width=500,
                                    window_height=250))
        self.title(self.i18n.add_book)
        self.resizable(False, False)
        self.name = tk.StringVar()
        self.page_number = tk.IntVar() 
        self.short_description = tk.StringVar()
        self.category = tk.StringVar()
        self.create_widgets()
        self.txt_name.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def adding_book(self):
        try:
            self.database_lib.add_book(name=self.name.get(), page_number=self.page_number.get(), short_description=self.short_description.get(),category= self.category.get())
            msg.showinfo(self.i18n.done, self.i18n.book_added)
            self.clear_text_boxes()
            self.txt_name.focus_set()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title=self.parent.window_title, message=self.i18n.failed_to_add_book)

    def clear_text_boxes(self):
        self.txt_name.delete(0, "end")
        self.txt_page_number.delete(0, "end")
        self.txt_short_description.delete(0, "end")
        self.txt_category.delete(0, "end")

    def create_widgets(self):
        self.lbl_name = ttk.Label(self, text=self.i18n.name)
        self.lbl_name.grid(column=0, row=0, padx=15, pady=15)
        self.lbl_page_number = ttk.Label(self, text=self.i18n.page_number)
        self.lbl_page_number.grid(column=0, row=1, padx=15, pady=(0, 15))
        self.lbl_short_description = ttk.Label(self, text=self.i18n.short_description)
        self.lbl_short_description.grid(column=0, row=2, padx=15, pady=(0, 15))
        self.lbl_category = ttk.Label(self, text=self.i18n.category)
        self.lbl_category.grid(column=0, row=3, padx=15, pady=(0, 15))

        self.txt_name = ttk.Entry(self, textvariable=self.name, width=35)
        self.txt_name.grid(column=1, row=0, padx=(0, 15), pady=15)
        self.txt_page_number = ttk.Entry(self, textvariable=self.page_number, width=35)
        self.txt_page_number.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        self.txt_short_description = ttk.Entry(self, textvariable=self.short_description, width=35)
        self.txt_short_description.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))
        self.txt_category = ttk.Combobox(self,textvariable=self.category, values=self.database_lib.get_categories(),width=35,state="readonly")
        self.txt_category.grid(column=1, row=3, padx=(0, 15), pady=(0, 15))

        self.btn_save = ttk.Button(self, text=self.i18n.add_book, command=self.adding_book)
        self.btn_save.grid(column=0, row=4, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()
