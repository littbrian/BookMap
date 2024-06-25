from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
import requests
import logging
from App.database import db
from App.models.books import Book


API_KEY = 'AIzaSyAfqpEiRKspeze-EBvXtHi6ouPGA5cZlc0' 

index_views = Blueprint('index_views', __name__, template_folder='../templates')

book_views = Blueprint('book_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    query = "bestsellers"
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=40&key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        books = response.json().get('items', [])
        if not books:
            return jsonify({"error": "No books found"}), 404
    else:
        return jsonify({"error": "Failed to fetch books"}), response.status_code

    return render_template('index.html', books=books)
@index_views.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=40&key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        books = response.json().get('items', [])
        if not books:
            return jsonify({"error": "No books found"}), 404
    else:
        return jsonify({"error": "Failed to fetch books"}), response.status_code

    tbrBooks = Book.query.filter_by(status='TBR').all()

    return render_template('index.html', books=books, tbrBooks=tbrBooks)

@index_views.route('/init', methods=['GET'])
def init():
        initialize()
        return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
        return jsonify({'status':'healthy'})
