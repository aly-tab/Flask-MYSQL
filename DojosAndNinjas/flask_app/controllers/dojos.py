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
    dojos = Dojo.get_all()
    print(dojos)

    for one_dojo in dojos:
        if one_dojo.id == idValue:
            name = one_dojo.name  

    data = {
        "id" : idValue
    }

    ninjas = Ninja.get_all(data)
    print(ninjas)   

    """
    ninjas = Dojo.get_dojos_with_ninjas(data)
    print(data)
    """


    return render_template('dojos.html', id_number=idValue, dname=name, ninjas=ninjas)

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

