import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import database_lib
import add_book
import book_list
import add_librarian
import librarian_list
import add_category
import category_list
import langpack
from centerscreen import center_screen_geometry

class MainWindoww:
    def __init__(self):
        self.win = tk.Tk()
        self.selected_language = tk.StringVar(value="en")
        self.i18n = langpack.I18N(self.selected_language.get())
        self.window_title = self.i18n.library_management_system
        self.win.geometry(center_screen_geometry(screen_width=self.win.winfo_screenwidth(),
                                    screen_height=self.win.winfo_screenheight(),
                                    window_width=1100,
                                    window_height=300))
        self.win.title(self.window_title)
        self.db = database_lib.LibraryManager()
        self.create_widgets()
        self.create_database()
        self.bind_widgets()


    def create_widgets(self):

        self.tab_library = ttk.LabelFrame(self.win, text=self.i18n.librarians, width=200, height=200)
        self.tab_books = ttk.LabelFrame(self.win, text=self.i18n.books, width=200, height=200)
        self.tab_category = ttk.LabelFrame(self.win, text=self.i18n.categories, width=200, height=200)

        self.btn_add_new_book = ttk.Button(self.tab_books, text=self.i18n.add_new_book, width=30, command=self.show_add_new_book_window)
        self.btn_show_book_list = ttk.Button(self.tab_books, text=self.i18n.show_book_list, width=30, command=self.show_book_list_window)
        self.btn_clear_database_books = ttk.Button(self.tab_books, text=self.i18n.clear_database_book, width=30, command=self.clear_database_book)

        self.btn_add_new_librarian = ttk.Button(self.tab_library, text=self.i18n.add_new_librarian, width=30, command=self.show_add_new_librarian_window)
        self.btn_show_librarian_list = ttk.Button(self.tab_library, text=self.i18n.show_librarian_list, width=30, command=self.show_librarian_list_window)
        self.btn_clear_database_librarian = ttk.Button(self.tab_library, text=self.i18n.clear_database_librarian, width=30, command=self.clear_database_librarian)

        self.btn_add_new_category = ttk.Button(self.tab_category, text=self.i18n.add_new_category, width=30, command=self.show_add_new_category_window)
        self.btn_show_category_list = ttk.Button(self.tab_category, text=self.i18n.show_category_list, width=30, command=self.show_category_list_window)
        self.btn_clear_database_category = ttk.Button(self.tab_category, text=self.i18n.clear_database_category, width=30, command=self.clear_database_category)

        self.tab_books.pack(side=tk.LEFT, padx=(30))
        self.tab_category.pack(side=tk.LEFT)
        self.tab_library.pack(side=tk.LEFT, padx=(30))
        

        self.btn_add_new_librarian.pack(padx=10, pady=(10, 0))
        self.btn_show_librarian_list.pack(padx=10, pady=(10, 0))
        self.btn_clear_database_librarian.pack(padx=10, pady=(10, 10))

        self.btn_add_new_category.pack(padx=10, pady=(10, 0))
        self.btn_show_category_list.pack(padx=10, pady=(10, 0))
        self.btn_clear_database_category.pack(padx=10, pady=(10, 10))

        self.btn_add_new_book.pack(padx=10, pady=(10, 0))
        self.btn_show_book_list.pack(padx=10, pady=(10, 0))
        self.btn_clear_database_books.pack(padx=10, pady=(10, 10))

        self.context_menu = tk.Menu(self.win, tearoff=False)
        self.context_menu.add_radiobutton(label="English", variable=self.selected_language, value="en",
                                          command=lambda: self.reload_gui_text("en"))
        self.context_menu.add_radiobutton(label="Türkçe", variable=self.selected_language, value="tr",
                                          command=lambda: self.reload_gui_text("tr"))

        

    

    def create_database(self):
        try:
            self.db.create_database()
        except sqlite3.Error as err:
            msg.showerror(title=self.window_title, message=self.i18n.failed_to_create_database)

    def reload_gui_text(self, language):
        self.i18n = langpack.I18N(language)
        self.win.title(self.i18n.title)
        self.tab_library.config(text=self.i18n.librarians)
        self.tab_books.config(text=self.i18n.books)
        self.tab_category.config(text=self.i18n.categories)
        self.btn_add_new_book.config(text=self.i18n.add_new_book)
        self.btn_show_book_list.config(text=self.i18n.show_book_list)
        self.btn_clear_database_books.config(text=self.i18n.clear_database_book)
        self.btn_add_new_librarian.config(text=self.i18n.add_new_librarian)
        self.btn_show_librarian_list.config(text=self.i18n.show_librarian_list)
        self.btn_clear_database_librarian.config(text=self.i18n.clear_database_librarian)
        self.btn_add_new_category.config(text=self.i18n.add_new_category)
        self.btn_show_category_list.config(text=self.i18n.show_category_list)
        self.btn_clear_database_category.config(text=self.i18n.clear_database_category)



    def exit_app():
        dialog_result = msg.askyesno(title=self.i18n.exit, message=self.i18n.are_you_sure_you_want_to_exit)
        if dialog_result:
            win.destroy()

    def clear_database_book(self):
        dialog_result = msg.askyesno(title=self.i18n.delete_database, message=self.i18n.clear_books_database)
        if dialog_result:
            try:
                self.db.clear_book_from_database()
                msg.showinfo(title=self.window_title, message=self.i18n.database_cleared)
            except sqlite3.Error as err:
                msg.showerror(title=self.window_title, message=self.i18n.failed_to_clear_database)

    def clear_database_librarian(self):
        dialog_result = msg.askyesno(title=self.i18n.delete_database, message=self.i18n.clear_librarians_database)
        if dialog_result:
            try:
                self.db.clear_librarian_from_database()
                msg.showinfo(title=self.window_title, message=self.i18n.database_cleared)
            except sqlite3.Error as err:
                msg.showerror(title=self.window_title, message=self.i18n.failed_to_clear_database)            

    def clear_database_category(self):
        dialog_result = msg.askyesno(title=self.i18n.delete_database, message=self.i18n.clear_categories_database)
        if dialog_result:
            try:
                self.db.clear_category_from_database()
                msg.showinfo(title=self.window_title, message=self.i18n.database_cleared)
            except sqlite3.Error as err:
                msg.showerror(title=self.window_title, message=self.i18n.failed_to_clear_database)    

    def show_add_new_book_window(self):
        self.win.withdraw()
        self.add_new = add_book.AddBook(parent=self)
        self.add_new.grab_set()

    def show_add_new_librarian_window(self):
        self.win.withdraw()
        self.add_new = add_librarian.AddLibrarian(parent=self)
        self.add_new.grab_set()    

    def show_add_new_category_window(self):
        self.win.withdraw()
        self.add_new = add_category.AddCategory(parent=self)
        self.add_new.grab_set()

    def show_book_list_window(self):
        self.book_list = book_list.BookList(parent=self)
        self.book_list.grab_set()

    def show_librarian_list_window(self):
        self.librarian_list = librarian_list.LibrarianList(parent=self)
        self.librarian_list.grab_set()  

    def show_category_list_window(self):
        self.category_list = category_list.CategoryList(parent=self)
        self.category_list.grab_set()

    def bind_widgets(self):
        self.win.bind("<Button-2>", self.show_context_menu)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)     

app = MainWindoww()
app.win.mainloop()
