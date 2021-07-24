from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite


@app.route('/authors')          
def index():
    authors = Author.get_all()
    print(authors)
    return render_template('index.html', authors=authors)  

@app.route('/books')          
def books():
    books = Book.get_all()
    print(books)
    return render_template('books.html', books=books) 

@app.route('/authors/<int:id>')          
def author_favorites(id):
    data = {
        "id" : id
    }
    author = Author.get_author_with_books(data)
    print(author)

    if author == 0:
        author = Author.get_author_by_id(data)
        print(author)

    books = Book.get_all()
    print(books)

    return render_template('author-favorites.html', author=author, books=books)  

@app.route('/books/<int:id>')          
def book_favorites(id):
    data = {
        "id" : id
    }
    book = Book.get_book_with_authors(data)
    print(book)

    if book == 0:
        book = Book.get_book_by_id(data)

    authors = Author.get_all() 
    print(authors)

    return render_template('book-favorites.html', book=book, authors=authors) 

@app.route('/authors/addauthor', methods=['POST'])          
def addauthor():
    print(request.form)
    data = {
        "name" : request.form['name'],
    }
    author = Author.save(data)
    print(author)

    return redirect('/authors')

@app.route('/books/addbook', methods=['POST'])          
def addbook():
    print(request.form)
    data = {
        "title" : request.form['title'],
        "pages" : request.form['pages']

    }

    book = Book.save(data)
    print(book)


    return redirect('/books')

@app.route('/authors/addauthorfavorite', methods=['POST'])          
def addauthorfavorite():
    print(request.form)

    author_id = request.form["authorid"]

    data = {
        "author_id" : request.form['authorid'],
        "book_id" : request.form['bookid']

    }

    favorite = Favorite.save(data)
    print(favorite)

    return redirect(f'/authors/{author_id}')

@app.route('/books/addbookfavorite', methods=['POST'])  
def addbookfavorite():
    print(request.form)
    book_id = request.form['bookid']

    data = {
        "author_id" : request.form['authorid'],
        "book_id" : request.form['bookid']

    }

    favorite = Favorite.save(data)
    print(favorite)

    return redirect(f'/books/{book_id}')
