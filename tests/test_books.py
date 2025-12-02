import unittest
from src.taskClass import Book, PrintedBook, EBook, User, Library


class TestBooks(unittest.TestCase):

    def test_book_creation(self):
        """Тест создания книги"""
        book = Book("1984", "Оруэлл", 1949)
        self.assertEqual(book.get_title(), "1984")
        self.assertEqual(book.get_author(), "Оруэлл")
        self.assertEqual(book.get_year(), 1949)
        self.assertTrue(book.is_available())

    def test_book_availability(self):
        """Тест доступности книги"""
        book = Book("1984", "Оруэлл", 1949)
        self.assertTrue(book.is_available())
        
        book.mark_as_taken()
        self.assertFalse(book.is_available())
        
        book.mark_as_returned()
        self.assertTrue(book.is_available())

    def test_printed_book(self):
        """Тест печатной книги"""
        printed_book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        self.assertEqual(printed_book.get_title(), "Война и мир")
        self.assertEqual(printed_book.pages, 1225)
        self.assertEqual(printed_book.condition, "хорошая")
        
        printed_book.repair()
        self.assertEqual(printed_book.condition, "новая")

    def test_ebook(self):
        """Тест электронной книги"""
        ebook = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
        self.assertEqual(ebook.get_title(), "Мастер и Маргарита")
        self.assertEqual(ebook.file_size, 5)
        self.assertEqual(ebook.format, "epub")
        self.assertTrue(ebook.is_available())

    def test_user_borrow_book(self):
        """Тест взятия книги пользователем"""
        user = User("Анна")
        book = Book("1984", "Оруэлл", 1949)
        
        result = user.borrow(book)
        self.assertTrue(result)
        self.assertFalse(book.is_available())
        self.assertEqual(len(user.get_borrowed_books()), 1)

    def test_user_return_book(self):
        """Тест возврата книги пользователем"""
        user = User("Анна")
        book = Book("1984", "Оруэлл", 1949)
        
        user.borrow(book)
        result = user.return_book(book)
        
        self.assertTrue(result)
        self.assertTrue(book.is_available())
        self.assertEqual(len(user.get_borrowed_books()), 0)


if __name__ == "__main__":
    unittest.main()

