from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User 
from flask_app.models.recipe import Recipe
from flask_app.controllers import users
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():

    data = {
       "id" : session['user_id']
    }

    user = User.get_by_id(data)
    print(user)

    recipes = Recipe.get_all()
    print(recipes)

    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    print(request.form)

    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made_on" : request.form["date"],
        "under_30" : request.form["selection"],
        "user_id" : session['user_id']
    }

    if not Recipe.validate_recipe(data):
        return redirect('/create')


    recipe = Recipe.save(data)
    print(recipe)

    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id" : id
    }

    recipe = Recipe.get_recipe(data)

    return render_template('edit.html', recipe=recipe)

@app.route('/edit_process/<int:id>', methods=['POST'])
def edit_process(id):
    print(request.form)

    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date_made_on" : request.form['date'],
        "under_30" : request.form['selection'],        
        "id" : id
    }

    if not Recipe.validate_recipe(data):
        return redirect(f'/edit/{id}')

    Recipe.update(data)

    return redirect(f'/edit/{ id }')

@app.route('/view/<int:id>')
def view(id):
    print(request.form)

    data = {
        "id" : id
    }

    recipe = Recipe.get_recipe(data)

    data2 = {
        "id" : session['user_id']
    }

    user = User.get_by_id(data2)

    return render_template('view.html', recipe=recipe, user=user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }

    Recipe.delete(data)

    return redirect('/dashboard')