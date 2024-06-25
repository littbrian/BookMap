from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for,flash
from App.models.books import Book
from App.database import db



book_views = Blueprint('book_views', __name__, template_folder='../templates')


@book_views.route('/addBooktoTBR', methods=['POST'])
def add_book_to_reading_list():
    book_id = request.form['id']
    title = request.form['title']
    authors = request.form['authors']
    published_date = request.form['published_date']
    image = request.form['image']
    status = request.form['status']

    # Check if the book already exists
    book = Book.query.filter_by(book_id=book_id).first()
    if book:
        book.status = status
        flash(f"Book {title} status updated to {status}!")
    else:
        # Create a new book entry
        book = Book(book_id=book_id, Title=title, Author=authors, Publication_Year=published_date, status=status, image=image)
        db.session.add(book)
        flash(f"Book {title} added to {status}!", 'success')

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f"Failed to add/update book {title}. Error: {e}", 'danger')

    return redirect(url_for('index_views.index_page'))

 


@book_views.route('/show_tbr', methods=['GET'])
def show_tbr():
    tbr_books = Book.query.filter_by(status='TBR').all()
    return jsonify([{
        "book_id": book.book_id,
        "Title": book.Title,
        "Author": book.Author,
        "Publication_Year": book.Publication_Year,
        "status": book.status
    } for book in tbr_books])


@book_views.route('/show_favorites', methods=['GET'])
def show_favorites():
    tbr_books = Book.query.filter_by(status='favorites').all()
    return jsonify([{
        "book_id": book.book_id,
        "Title": book.Title,
        "Author": book.Author,
        "Publication_Year": book.Publication_Year,
        "status": book.status
    } for book in tbr_books])

@book_views.route('/books', methods=['GET'])
def list_books_by_status():
    favoriteBooks = Book.query.filter_by(status='favorites').all()
    tbrBooks = Book.query.filter_by(status='to read').all()
    readBooks = Book.query.filter_by(status='read').all()
    currentReadBooks = Book.query.filter_by(status='current read').all()

    return render_template('books.html', 
                           favoriteBooks=favoriteBooks, 
                           tbrBooks=tbrBooks, 
                           readBooks=readBooks, 
                           currentReadBooks=currentReadBooks)

