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

if __name__=="__main__":       
    app.run(debug=True)    
