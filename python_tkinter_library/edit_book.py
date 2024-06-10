import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import database_lib
from centerscreen import center_screen_geometry


class EditBook(tk.Toplevel):
    def __init__(self, parent, rowid, gid, name, page_number, short_description, category):
        super().__init__()
        self.database_lib = database_lib.LibraryManager()
        self.parent = parent
        self.geometry("500x250")
        self.i18n = parent.i18n
        self.title(f"{name}")
        self.resizable(False, False)
        self.name = tk.StringVar(value=name)
        self.page_number = tk.IntVar(value=page_number)
        self.short_description = tk.StringVar(value=short_description)
        self.category = tk.StringVar(value=category)
        self.gid = gid
        self.rowid = rowid  
        self.create_widgets()
        self.txt_name.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            self.database_lib.edit_book(gid=self.gid, name=self.name.get(), page_number=self.page_number.get(), short_description=self.short_description.get(), category=self.category.get())
            self.parent.tv.item(self.rowid, values=(self.gid, self.name.get(), self.page_number.get(), self.short_description.get(),self.category.get()))
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title=self.i18n.error, message=self.i18n.failed_to_changes)

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
        self.txt_category = ttk.Entry(self, textvariable=self.category, width=35)
        self.txt_category.grid(column=1, row=3, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self, text=self.i18n.update, command=self.update_values)
        self.btn_update.grid(column=0, row=4, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.destroy()
