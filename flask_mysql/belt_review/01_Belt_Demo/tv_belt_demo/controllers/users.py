from tv_belt_demo import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from tv_belt_demo.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hashed_password
    }

    session['user_id'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # Run the data through the login validator
    login_validation = User.validate_login(request.form)
    # If it returns false, redirect away.
    if not login_validation:
        return redirect('/')
    # If it doesn't return false, then it actually returned
    # the user from the database that is trying to log in
    # So we'll store its user id in session
    session['user_id'] = login_validation.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')
