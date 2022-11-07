from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.friends import Friend


@app.route('/')
def index():
    return render_template("index.html", all_friends=Friend.get_all())


@app.route('/create_friend', methods=['POST'])
def create_friend():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation']
    }
    Friend.save(data)
    return redirect('/')
