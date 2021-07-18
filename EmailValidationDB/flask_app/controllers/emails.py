from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.email import Email 

@app.route('/')          
def index():
    return render_template('index.html') 

@app.route('/addemail', methods=['POST'])
def addemail():
    print(request.form)

    data = {
        "email" : request.form["email"]
    }

    email = Email.save(data)
    print(email)

    validation = Email.validate_email(data)

    session["validation"] = validation

    return redirect ('/success')

@app.route('/success')
def success():
    
    emails = Email.get_all()
    print(emails)

    if session['validation'] == False:
        b_color = 'red'
        color = 'black'
    else:
        b_color = 'green'
        color = 'white'

    return render_template('list.html', emails=emails, b_color=b_color, color=color)