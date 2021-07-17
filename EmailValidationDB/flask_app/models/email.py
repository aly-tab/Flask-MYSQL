from flask_app.config.mysqlconnection import connectToMySQL

class Email:
	def __init__( self , data ):
		self.id = data['id']
		self.email = data['email']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']


