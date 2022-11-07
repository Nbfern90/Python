from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/register', methods=["POST"])
def create():

    if not User.validate_user(request.form):
        print("not valid")
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": pw_hash

    }
    user_id = User.save(data)
    # session['user_id'] = user_id
    return redirect('/')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_login', methods=['POST'])
def login():
    data = {"email": request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Inavalid Email or Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def main_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', people=User.get_by_id(data), users=Recipe.get_recipe_with_users())
