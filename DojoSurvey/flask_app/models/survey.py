from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
	def __init__( self , data ):
		self.id = data['id']
		self.name = data['name']
		self.location = data['location']
		self.favorite_language = data['favorite_language']
		self.comment = data['comment']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

	@classmethod
	def get_all(cls):
		query = "SELECT * FROM survey;"

		results = connectToMySQL('dojo_survey').query_db(query)
		surveys = []
		for survey in results:
			surveys.append( cls(survey) )
		return surveys

	@classmethod
	def save(cls, data):
		query = "INSERT INTO survey ( name, location, favorite_language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
		return connectToMySQL('dojo_survey').query_db( query, data )

	@staticmethod
	def validate_survey(survey):
		is_valid = True
		if len(survey['name']) < 3:
			flash("Name must be at least 3 characters.")	
			is_valid = False 
		return is_valid

