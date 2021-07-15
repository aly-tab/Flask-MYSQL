from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja 

@app.route('/dojos')          
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos=dojos)  

@app.route('/dojos/createdojo', methods=['POST'])
def createdojo():
    print(request.form)
    data = {
        "dname" : request.form["dname"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', all_dojos=dojos)

@app.route('/dojos/<int:idValue>')
def dojos(idValue):
    data = {
        "id" : idValue
    }

    dojo = Dojo.get_dojos_with_ninjas(data)
    print(data)

    return render_template('dojos.html', id_number=idValue, dojo=dojo)

@app.route('/ninjas/createninja', methods=['POST'])
def createninja():
    print(request.form)

    dojos = Dojo.get_all()
    print(dojos)

    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["did"]

    }
    Ninja.save(data)
    return redirect('/dojos')

