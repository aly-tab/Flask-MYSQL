from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__( self , data ):
        self.id =  data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.friendships_id =  data['friendships.id']
        self.message = data['message']
        self.friendships_created_at= data['friendships.created_at']
        self.friendships_updated_at = data['friendships.updated_at']
        self.sender_id = data['sender_id']
        self.reciever_id = data['reciever_id']

    @classmethod
    def get_user_messages(cls, data):
        query = "SELECT * FROM users LEFT JOIN friendships ON users.id = friendships.sender_id WHERE friendships.reciever_id = %(id)s;"
        results = connectToMySQL('private_wall_schema').query_db( query , data )

        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages
