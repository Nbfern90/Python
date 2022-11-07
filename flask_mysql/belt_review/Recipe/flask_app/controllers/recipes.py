from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app


@app.route('/logout')
def logout():
    session.clear()
    return render_template("/index.html")


@app.route('/create')
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/create.html', people=User.get_all())


@app.route('/new_recipe', methods=['POST'])
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect('/create')

    recipe = {
        'name': request.form['name'],
        'description': request.form['description'],
        'under_30': request.form['under_30'],
        'instructions': request.form['instructions'],
        'user_id': session['user_id']
    }

    Recipe.save(recipe)

    return redirect('/dashboard')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_to_edit = Recipe.get_one({'id': id})
    data = {
        'id': session['user_id']
    }

    return render_template("edit.html", users=recipe_to_edit, people=User.get_by_id(data))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect('/create')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'under_30': request.form['under_30'],
        'instructions': request.form['instructions'],
        'user_id': session['user_id']
    }

    Recipe.edit(data)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    Recipe.delete({'id': id})
    return redirect('/dashboard')


@app.route('/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/')
    i = Recipe.get_one({'id': id})
    data = {
        'id': session['user_id']
    }

    return render_template("show.html", i=i, people=User.get_by_id(data))
