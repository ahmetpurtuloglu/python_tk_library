import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import database_lib
import edit_category
from centerscreen import center_screen_geometry


class CategoryList(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = database_lib.LibraryManager()
        self.parent = parent
        self.i18n = parent.i18n
        self.geometry("1200x500+500+250")
        self.title(self.i18n.category_list)
        self.create_widgets()
        self.bind_widgets()
        self.list_categories()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def list_categories(self):
        for category in self.db.list_categories():
            self.tv.insert(parent="", index="end", values=category)

    def delete_category(self, event):
        answer = msg.askyesno(title=self.i18n.confirm_delete, message=self.i18n.are_you_sure)
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_category(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        region = self.tv.identify("region", event.x, event.y)
        if region != "cell":
            return

        selected_row_id = self.tv.selection()[0]
        selected_grade_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = edit_category.EditCategory(parent=self,
                                                        rowid=selected_row_id,
                                                        gid=selected_grade_row[0],
                                                        name=selected_grade_row[1])
        self.edit_selected.grab_set()

    def create_widgets(self):
        self.tv = ttk.Treeview(self, height=10, show="headings", selectmode="extended")
        self.tv["columns"] = ("id", "name")
        self.tv.pack(fill="both", expand=True)

        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("name", text=self.i18n.name, anchor="center")

        self.tv.column("id", anchor="center", width=45, stretch="no")
        self.tv.column("name", anchor="w", width=135)

        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.tv.bind("<Delete>", self.delete_category)  
        self.tv.bind("<Double-1>", self.show_edit_window)

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()
