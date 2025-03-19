import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        book_lover = BookLover( "Sam V", "samuelv@gmail.com", "mystery")
        book_lover.add_book("The Great Gatsby", 5)
        self.assertIn("The Great Gatsby", book_lover.book_list['book_name'].values)
        
        
    def test_2_add_book(self):
        book_lover = BookLover("Tony Bennet", "tb5@gmail.com", "sports")
        book_lover.add_book("Bible", 4)
        book_lover.add_book("Bible", 4)
        self.assertEqual(book_lover.book_list['book_name'].value_counts().get("Bible", 0), 1)
        
    
    def test_3_has_read(self):
        book_lover = BookLover("Alice", "alice@gmail.com", "fantasy")
        book_lover.add_book("Harry Potter", 5)
        self.assertTrue(book_lover.has_read("Harry Potter"))
        
    def test_4_has_read(self):
        book_lover = BookLover("Cory", "Cory@example.com", "thriller")
        self.assertFalse(book_lover.has_read("Conjuring"))
        
        
    def test_5_num_books_read(self):
        book_lover = BookLover("Charlie", "charlie@gmail.com", "history")
        book_lover.add_book("Cat in the Hat", 5)
        book_lover.add_book("World War 2", 4)
        book_lover.add_book("1776", 3)
        self.assertEqual(book_lover.num_books_read(), 3)
    
    def test_6_fav_books(self):
        book_lover = BookLover("Dave", "dave@gmail.com", "biography")
        book_lover.add_book("Winston Churchill", 5)
        book_lover.add_book("Elon Musk", 2)
        book_lover.add_book("Donald Trump", 4)
        fav_books = book_lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
 

if __name__ == '__main__':
    
    unittest.main(verbosity=3)