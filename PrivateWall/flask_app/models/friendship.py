from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Friendship:
    def __init__( self , data ):
        self.id =  data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.reciever_id = data['reciever_id']

    @classmethod
    def send_message(cls, data):
        query = "INSERT INTO friendships (message , created_at , updated_at , sender_id , reciever_id) VALUES (%(message)s, NOW() , NOW() , %(sender_id)s, %(reciever_id)s );"
        return connectToMySQL('private_wall_schema').query_db( query, data )

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM friendships WHERE id = %(id)s;"
        return connectToMySQL('private_wall_schema').query_db( query, data )
