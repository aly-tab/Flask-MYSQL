from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Friendship:
    def __init__( self , data ):
        self.id =  data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.reciever_id = data['reciever_id']

        self.sender = []

    @classmethod
    def send_message(cls, data):
        query = "INSERT INTO friendships (message , created_at , updated_at , sender_id , reciever_id) VALUES (%(message)s, NOW() , NOW() , %(sender_id)s, %(reciever_id)s );"
        return connectToMySQL('private_wall_schema').query_db( query, data )

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM friendships WHERE id = %(id)s;"
        return connectToMySQL('private_wall_schema').query_db( query, data )

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM friendships LEFT JOIN users On users.id = sender_id WHERE reciever_id = %(id)s ;"
        results = connectToMySQL('private_wall_schema').query_db( query, data )

        messages = []

        for row_in_db in results:
            one_message = cls(row_in_db)

            user_data = {
                "id" : row_in_db['users.id'],
                "first_name" : row_in_db['first_name'],
                "last_name" : row_in_db['last_name'],
                "email" : row_in_db['email'],
                "password" : row_in_db['password'],
                "created_at" : row_in_db['users.created_at'],
                "updated_at" : row_in_db['users.updated_at']
            }

            one_message.sender = User(user_data)
            messages.append(one_message)
        return messages

