from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
	def __init__( self , data ):
		self.id = data['id']
		self.author_id = data['author_id']
		self.book_id = data['book_id']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

#==================================================================================================#

	@classmethod
	def save(cls, data ):
		query = "INSERT INTO favorites ( author_id, book_id , created_at , updated_at ) VALUES ( %(author_id)s , %(book_id)s , NOW() , NOW() );"
		return connectToMySQL('books_schema').query_db( query, data )

