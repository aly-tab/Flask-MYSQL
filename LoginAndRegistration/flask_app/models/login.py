from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Login:
    def __init__( self , data ):
        self.id =  data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO logins (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW() , NOW() );"
        return connectToMySQL("login_schema").query_db(query, data)

    @classmethod
    def get_by_email(cls, data ):
        query = "SELECT * FROM logins WHERE email = %(email)s;"
        result = connectToMySQL("login_schema").query_db(query,data)

        if len(result) < 1:
                return False
        return cls(result[0])           
        
    @staticmethod
    def validate_email_and_password( data ):
        is_valid = True	

        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif data['password'] != data['confirm-password']:
            flash("Passwords do not match!")
            is_valid = False
        else: 
            flash("You successfully registered!")
                
        return is_valid	


