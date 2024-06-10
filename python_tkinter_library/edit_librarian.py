import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import database_lib
from centerscreen import center_screen_geometry


class EditLibrarian(tk.Toplevel):
    def __init__(self, parent, rowid, gid, name, age, gender):
        super().__init__()
        self.database_lib = database_lib.LibraryManager()
        self.parent = parent
        self.geometry("440x200")
        self.i18n = parent.i18n
        self.title(f"{name}")
        self.resizable(False, False)
        self.name = tk.StringVar(value=name)
        self.age = tk.IntVar(value=age)
        self.gender = tk.StringVar(value=gender)
        self.gid = gid
        self.rowid = rowid  
        self.create_widgets()
        self.txt_name.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            self.database_lib.edit_librarian(gid=self.gid, name=self.name.get(), age=self.age.get(), gender=self.gender.get())
            self.parent.tv.item(self.rowid, values=(self.gid, self.name.get(), self.age.get(), self.gender.get()))
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title=self.i18n.error, message=self.i18n.failed_to_changes)

    def create_widgets(self):
        self.lbl_name = ttk.Label(self, text=self.i18n.name)
        self.lbl_name.grid(column=0, row=0, padx=15, pady=15)
        self.lbl_age = ttk.Label(self, text=self.i18n.age)
        self.lbl_age.grid(column=0, row=1, padx=15, pady=(0, 15))
        self.lbl_gender = ttk.Label(self, text=self.i18n.gender)
        self.lbl_gender.grid(column=0, row=2, padx=15, pady=(0, 15))

        self.txt_name = ttk.Entry(self, textvariable=self.name, width=35)
        self.txt_name.grid(column=1, row=0, padx=(0, 15), pady=15)
        self.txt_age = ttk.Entry(self, textvariable=self.age, width=35)
        self.txt_age.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        self.txt_gender= ttk.Entry(self, textvariable=self.gender, width=35)
        self.txt_gender.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self, text=self.i18n.update, command=self.update_values)
        self.btn_update.grid(column=0, row=3, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.destroy()
