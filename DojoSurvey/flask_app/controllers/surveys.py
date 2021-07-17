from flask_app import app
from flask import render_template, request, redirect, session 
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print(request.form)

    data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"],
    }

    if not Survey.validate_survey(data):
        return redirect('/')


    survey = Survey.save(data)
    print(survey)

    session["name"] = request.form["name"]

    return redirect("/result")


@app.route('/result')
def result():

    surveys = Survey.get_all()
    print(surveys)

    for survey in surveys:
        if survey.name == session["name"]:
            id = survey.id

    return render_template('result.html', surveys=surveys, id=id)
