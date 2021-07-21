from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User 
from flask_app.controllers import recipes
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')          
def index():
    return render_template('index.html') 

@app.route('/register', methods = ['POST'])
def register():
    print(request.form)

    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm-password" : request.form["confirm-password"],        
    }

    validation = User.validate_email_and_password(data)

    if validation == False: 
        redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : pw_hash
    }

    user_id = User.save(data)

    session['user_id'] = user_id

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():

    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)

    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user.id       
    return redirect('/dashboard')



