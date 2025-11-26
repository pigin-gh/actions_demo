class Book:

    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        status = "доступна" if self.__available else "взята"
        return f"Книга: {self.__title}, Автор: {self.__author}, Год: {self.__year}, Статус: {status}"


class PrintedBook(Book):

    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Страниц: {self.pages}, Состояние: {self.condition}"

# Добавил прикольчик в кодик пу пу пу пу


class EBook(Book):

    def __init__(self, title, author, year, file_size, format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format

    def download(self):
        print(f"Книга {self.get_title()} загружается...")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Размер: {self.file_size} МБ, Формат: {self.format}"


class User:

    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            return True
        return False

    def show_books(self):
        if not self.__borrowed_books:
            print(f"{self.name} не имеет взятых книг")
        else:
            print(f"Книги {self.name}:")
            for book in self.__borrowed_books:
                print(f"  - {book.get_title()} ({book.get_author()})")

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()


class Librarian(User):

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, title):
        library.remove_book(title)

    def register_user(self, library, user):
        library.add_user(user)


class Library:

    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        book = self.find_book(title)
        if book:
            self.__books.remove(book)
            return True
        return False

    def add_user(self, user):
        if user not in self.__users:
            self.__users.append(user)

    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def find_user(self, name):
        for user in self.__users:
            if user.name == name:
                return user
        return None

    def show_all_books(self):
        if not self.__books:
            print("В библиотеке нет книг")
        else:
            print("Все книги в библиотеке:")
            for book in self.__books:
                print(f"  - {book}")

    def show_available_books(self):
        available = [book for book in self.__books if book.is_available()]
        if not available:
            print("Нет доступных книг")
        else:
            print("Доступные книги:")
            for book in available:
                print(f"  - {book}")

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book:
            print(f"Книга '{title}' не найдена в библиотеке")
            return False

        if not user:
            print(f"Пользователь '{user_name}' не зарегистрирован")
            return False

        if user.borrow(book):
            print(f"Книга '{title}' выдана пользователю {user_name}")
            return True
        else:
            print(f"Книга '{title}' недоступна")
            return False

    def return_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book:
            print(f"Книга '{title}' не найдена в библиотеке")
            return False

        if not user:
            print(f"Пользователь '{user_name}' не зарегистрирован")
            return False

        if user.return_book(book):
            print(f"Книга '{title}' возвращена пользователем {user_name}")
            return True
        else:
            print(f"Пользователь {user_name} не брал книгу '{title}'")
            return False


if __name__ == '__main__':
    lib = Library()

    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook(
        "Преступление и наказание",
        "Достоевский",
        1866,
        480,
        "плохая")

    user1 = User("Анна")
    librarian = Librarian("Мария")

    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    librarian.register_user(lib, user1)

    lib.lend_book("Война и мир", "Анна")

    user1.show_books()

    lib.return_book("Война и мир", "Анна")

    b2.download()

    b3.repair()
    print(b3)
