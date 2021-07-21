from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__( self , data ):
        self.id =  data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"

        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name, description, instructions, date_made_on, under_30, created_at, updated_at, user_id ) VALUES ( %(name)s , %(description)s , %(instructions)s , %(date_made_on)s , %(under_30)s , NOW() , NOW() , %(user_id)s );"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s , description = %(description)s , instructions = %(instructions)s , date_made_on = %(date_made_on)s , under_30 = %(under_30)s , created_at = NOW() , updated_at = NOW() WHERE id = %(id)s ;"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
	    query = "DELETE FROM recipes WHERE id = %(id)s;"
	    return connectToMySQL('recipes_schema').query_db( query, data )

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0]) 

    @staticmethod
    def validate_recipe( data ):
        is_valid = True	

        if len(data['name']) < 3:
            flash("The name is too short!")
            is_valid = False
        if len(data['description']) < 7:
            flash("The description is too short!")
            is_valid = False
        if len(data['instructions']) < 7:
            flash("The instructions is too short!")
            is_valid = False
        if data['date_made_on'] == '':
            flash("No date was given!")
            is_valid = False         
        if is_valid == True: 
            flash("Your edit was successful!")
                
        return is_valid	

                                                                                                                      