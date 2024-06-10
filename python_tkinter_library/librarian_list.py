import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import database_lib
import edit_librarian
from centerscreen import center_screen_geometry


class LibrarianList(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = database_lib.LibraryManager()
        self.parent = parent
        self.i18n = parent.i18n
        self.geometry("1200x500+500+250")
        self.title(parent.window_title)
        self.create_widgets()
        self.bind_widgets()
        self.list_librarians()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def list_librarians(self):
        for librarian in self.db.list_librarians():
            self.tv.insert(parent="", index="end", values=librarian)

    def delete_librarian(self, event):
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row(s)?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_librarian(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        region = self.tv.identify("region", event.x, event.y)
        if region != "cell":
            return

        selected_row_id = self.tv.selection()[0]
        selected_grade_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = edit_librarian.EditLibrarian(parent=self,
                                                 rowid=selected_row_id,
                                                 gid=selected_grade_row[0],
                                                 name=selected_grade_row[1],
                                                 age=selected_grade_row[2],
                                                 gender=selected_grade_row[3])
        self.edit_selected.grab_set()

    def create_widgets(self):
        self.tv = ttk.Treeview(self, height=10, show="headings", selectmode="extended")
        self.tv["columns"] = ("id", "name", "age", "gender")
        self.tv.pack(fill="both", expand=True)

        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("name", text="Name", anchor="center")
        self.tv.heading("age", text="Age", anchor="center")
        self.tv.heading("gender", text="Gender", anchor="center")

        self.tv.column("id", anchor="center", width=45, stretch="no")
        self.tv.column("name", anchor="w", width=135)
        self.tv.column("age", anchor="w", width=135)
        self.tv.column("gender", anchor="center", width=135)

        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.tv.bind("<Delete>", self.delete_librarian)  
        self.tv.bind("<Double-1>", self.show_edit_window)  

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()
