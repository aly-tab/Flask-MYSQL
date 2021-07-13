from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)    
@app.route('/users')          
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)  

@app.route('/users/new')  
def new():
    return render_template('new.html')  

@app.route('/users/adduser', methods=['POST'])  
def adduser():
    print(request.form)
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<idValue>') 
def show(idValue):
    id_number = idValue
    users = User.get_all()
    print(users)

    all_users = users
    for one_user in all_users:
        if one_user.id == int(id_number):
            first_name = one_user.first_name
            last_name = one_user.last_name
            email = one_user.email
            created_at = one_user.created_at
            updated_at = one_user.updated_at


    return render_template('show.html', id_number=id_number, first_name=first_name, last_name=last_name, email=email, created_at=created_at, updated_at=updated_at)

@app.route('/users/<idValue>/edit') 
def edit(idValue):
    id_number = idValue
    users = User.get_all()
    print(users)

    all_users = users
    for one_user in all_users:
        if one_user.id == int(idValue):
            first_name = one_user.first_name
            last_name = one_user.last_name
            email = one_user.email
    return render_template('edit.html', id_number=id_number, first_name=first_name, last_name=last_name, email=email)


@app.route('/users/<idValue>/update', methods=['POST'])
def update(idValue):
    print(request.form)
    id_value = int(idValue)
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id_value" : id_value
    }

    User.update(data)
    return redirect('/users')

@app.route('/users/<idValue>/delete')
def delete(idValue):
    id_value = int(idValue)
    data = {
        "id_value" : id_value
    }

    User.delete(data)
    return redirect('/users')
    

if __name__=="__main__":       
    app.run(debug=True)    
