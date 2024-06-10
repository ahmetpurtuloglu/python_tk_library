import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import database_lib
from centerscreen import center_screen_geometry

class AddCategory(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.database_lib = database_lib.LibraryManager()
        self.parent = parent
        self.i18n = parent.i18n
        self.geometry(center_screen_geometry(screen_width=parent.win.winfo_screenwidth(),
                                    screen_height=parent.win.winfo_screenheight(),
                                    window_width=420,
                                    window_height=150))
        self.title(self.i18n.add_category)
        self.resizable(False, False)
        self.name = tk.StringVar()
        self.create_widgets()
        self.txt_name.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def adding_category(self):
        try:
            self.database_lib.add_category(name=self.name.get())
            msg.showinfo(self.i18n.done, self.i18n.category_added)
            self.clear_text_boxes()
            self.txt_name.focus_set()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title=self.parent.window_title, message=self.i18n.failed_to_add_category)

    def clear_text_boxes(self):
        self.txt_name.delete(0, "end")

    def create_widgets(self):
        self.lbl_name = ttk.Label(self, text=self.i18n.name)
        self.lbl_name.grid(column=0, row=0, padx=15, pady=15)

        self.txt_name = ttk.Entry(self, textvariable=self.name, width=35)
        self.txt_name.grid(column=1, row=0, padx=(0, 15), pady=15)

        self.btn_save = ttk.Button(self, text=self.i18n.add_category, command=self.adding_category)
        self.btn_save.grid(column=0, row=4, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()
