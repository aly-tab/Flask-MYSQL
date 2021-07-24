from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
	def __init__( self , data ):
		self.id = data['id']
		self.name = data['name']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']
		
		self.books = []  		       

	@classmethod
	def get_all(cls):
		query = "SELECT * FROM authors;"

		results = connectToMySQL('books_schema').query_db(query)
		authors = []
		for author in results:
			authors.append( cls(author) )
		return authors

	@classmethod
	def save(cls, data ):
		query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
		return connectToMySQL('books_schema').query_db( query, data )

	@classmethod
	def get_author_by_id(cls, data):
		query = "SELECT * FROM authors WHERE id = %(id)s;"
		result = connectToMySQL('books_schema').query_db( query, data )

		if len(result) < 1:
			return False
		return cls(result[0]) 

#=============================================================================================================#

	@classmethod
	def get_author_with_books(cls, data):
		query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE author_id = %(id)s;"
		results = connectToMySQL('books_schema').query_db( query , data )

		if len(results) == 0:
			return 0	
		else:
			author = cls(results[0])
			for row_from_db in results:
				books_data = {
					"id" : row_from_db["books.id"],
					"title" : row_from_db["title"],
					"num_of_pages" : row_from_db["num_of_pages"],
					"created_at" : row_from_db["books.created_at"],
					"updated_at" : row_from_db["books.updated_at"]		
				}
				author.books.append(book.Book( books_data) )
			return author
