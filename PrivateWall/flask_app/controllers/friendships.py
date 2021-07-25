from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.controllers import users
from flask_app.models.user import User
from flask_app.models.friendship import Friendship 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():

    data = {
       "id" : session['user_id']
    }

    user = User.get_by_id(data)
    print(user)

    users = User.get_all_but_user(data)
    print(users)

    messages = Friendship.get_all(data)
    print(messages)

    num = len(messages)

    print(len(messages))

    return render_template('dashboard.html', user=user, users=users, messages=messages, num=num)

@app.route('/send_message', methods=['POST'])
def send_message():

    data = {
        "message" : request.form["message"],
        "sender_id" : session['user_id'],
        "reciever_id" : request.form["reciever_id"]
    }

    Friendship.send_message(data)

    return redirect('/dashboard')

@app.route('/delete_message/<int:idNum>')
def delete_message(idNum): 
    data = {
        "id" : idNum
    }

    Friendship.delete_message(data)
    
    return redirect('/dashboard')
