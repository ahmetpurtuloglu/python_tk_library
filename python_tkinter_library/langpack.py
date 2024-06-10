import glob

class I18N:
    def __init__(self, language, load_from_file=True):
        if load_from_file:
            if language in self.get_available_languages():
                self.load_data_from_file(language)
            else:
                raise NotImplementedError("Unsupported language. Add missing language file.")
        else:
            if language == "en":
                self.load_data_in_english()
            elif language == "tr":
                self.load_data_in_turkish()
            else:
                raise NotImplementedError("Unsupported language.")

    def load_data_from_file(self, lang):
        lang_data = {}
        lang_file = f"data_{lang}.lng"
        with open(file=lang_file, encoding="utf-8") as f:
            for line in f:
                (key, val) = line.strip().split("=")
                lang_data[key] = val

        self.name = lang_data["name"]
        self.page_number = lang_data["page_number"]
        self.short_description = lang_data["short_description"]
        self.category = lang_data["category"]
        self.age = lang_data["age"]
        self.gender = lang_data["gender"]
        self.add_book = lang_data["add_book"]
        self.add_librarian = lang_data["add_librarian"]
        self.add_category = lang_data["add_category"]
        self.edit_book = lang_data["edit_book"]
        self.edit_category = lang_data["edit_category"]
        self.edit_librarian = lang_data["edit_librarian"]
        self.delete_book = lang_data["delete_book"]
        self.delete_librarian = lang_data["delete_librarian"]
        self.book_list = lang_data["book_list"]
        self.category_list = lang_data["category_list"]
        self.librarian_list = lang_data["librarian_list"]
        self.delete_book = lang_data["delete_book"]
        self.delete_category = lang_data["delete_category"]
        self.delete_librarian = lang_data["delete_librarian"]
        self.done = lang_data["done"]
        self.book_added = lang_data["book_added"]
        self.failed_to_add_book = lang_data["failed_to_add_book"]
        self.category_added = lang_data["category_added"]
        self.failed_to_add_category = lang_data["failed_to_add_category"]
        self.librarian_added = lang_data["librarian_added"]
        self.failed_to_add_librarian = lang_data["failed_to_add_librarian"]
        self.confirm_delete = lang_data["confirm_delete"]
        self.are_you_sure = lang_data["are_you_sure"]
        self.error = lang_data["error"]
        self.failed_to_changes = lang_data["failed_to_changes"]
        self.update = lang_data["update"]
        self.library_management_system = lang_data["library_management_system"]
        self.librarians = lang_data["librarians"]
        self.books = lang_data["books"]
        self.categories = lang_data["categories"]
        self.add_new_book = lang_data["add_new_book"]
        self.add_new_category = lang_data["add_new_category"]
        self.add_new_librarian = lang_data["add_new_librarian"]
        self.show_book_list = lang_data["show_book_list"]
        self.show_category_list = lang_data["show_category_list"]
        self.show_librarian_list = lang_data["show_librarian_list"]
        self.clear_database_book = lang_data["clear_database_book"]
        self.clear_database_category = lang_data["clear_database_category"]
        self.clear_database_librarian = lang_data["clear_database_librarian"]
        self.failed_to_clear_database = lang_data["failed_to_clear_database"]
        self.exit = lang_data["exit"]
        self.are_you_sure_you_want_to_exit = lang_data["are_you_sure_you_want_to_exit"]
        self.delete_database = lang_data["delete_database"]
        self.database_cleared = lang_data["database_cleared"]
        self.clear_books_database = lang_data["clear_books_database"]
        self.clear_categories_database = lang_data["clear_categories_database"]
        self.clear_librarians_database = lang_data["clear_librarians_database"]
        self.title = lang_data["title"]



    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")
        language_codes = []

        for f in language_files:
            language_code = f.replace("data_", "").replace(".lng", "")
            language_codes.append(language_code)

        return language_codes