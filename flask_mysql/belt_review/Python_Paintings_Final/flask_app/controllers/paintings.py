from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.painting import Painting
from flask_app import app


@app.route('/logout')
def logout():
    session.clear()
    return render_template("/index.html")


@app.route('/create')
def create_painting():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("/create.html", people=User.get_all())


@app.route('/new_painting', methods=['POST'])
def new_painting():
    if 'user_id' not in session:
        return redirect('/')

    if not Painting.validate_painting(request.form):
        return redirect('/create')

    painting = {
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'user_id': session['user_id']
    }

    Painting.save(painting)

    return redirect('/dashboard')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    painting_to_edit = Painting.get_one({'id': id})
    data = {
        'id': session['user_id']
    }

    return render_template("edit.html", users=painting_to_edit, people=User.get_by_id(data))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Painting.validate_painting(request.form):
        return redirect(f'/edit/{id}')

    data = {
        'id': id,
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'user_id': session['user_id']
    }

    Painting.edit(data)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    Painting.delete({'id': id})
    return redirect('/dashboard')


@app.route('/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/')
    i = Painting.get_one({'id': id})
    data = {
        'id': session['user_id']
    }

    return render_template("show.html", i=i, people=User.get_by_id(data))
