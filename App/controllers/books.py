from App.models.books import Book
from App.database import db

def create_book(ISBN, Title, Author, Publisher, Publication_Year, Price, status):
    book = Book(ISBN, Title, Author, Publisher, Publication_Year, Price, status, image)
    db.session.add(book)
    db.session.commit()
    return book    

def get_book(ISBN):
    book = Book.query.filter_by(ISBN=ISBN).first()
    return book   

def get_all_books():
    books = Book.query.all()
    return books

def update_book(ISBN, Title, Author, Publisher, Publication_Year, Price, status):
    book = Book.query.filter_by(ISBN=ISBN).first()
    book.Title = Title
    book.Author = Author
    book.Publisher = Publisher
    book.Publication_Year = Publication_Year
    book.Price = Price
    book.status = status
    db.session.commit()
    return book

def add_book_to_reading_list(book_id):
    # Find the book by book_id or create a new one if it doesn't exist
    book = Book.query.filter_by(id=book_id).first()
    if not book:
        # Create a new book entry with the status set to 'TBR'
        new_book = Book(id=book_id, status='TBR')
        db.session.add(new_book)
    else:
        # Update the status of the existing book to 'TBR'
        book.status = 'TBR'

    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False

def delete_book(ISBN):
    book = Book.query.filter_by(ISBN=ISBN).first()
    db.session.delete(book)
    db.session.commit()
    return book

