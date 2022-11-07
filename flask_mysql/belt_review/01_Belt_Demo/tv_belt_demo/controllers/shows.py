from tv_belt_demo import app
from flask import render_template, redirect, request, session
from tv_belt_demo.models.user import User
from tv_belt_demo.models.show import Show


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    logged_in_user = User.get_user_by_id({'id': session['user_id']})

    all_shows = Show.get_all()

    return render_template('dashboard.html', user_name=logged_in_user.first_name, all_shows=all_shows)


@app.route('/show/<int:show_id>')
def show_info(show_id):
    if 'user_id' not in session:
        return redirect('/')

    show = Show.get_one({'id': show_id})

    if not show:
        return redirect('/dashboard')

    return render_template('show_info.html', show=show)


@app.route('/new')
def new_show():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('new_show.html')


@app.route('/create', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/')

    if not Show.validate_show(request.form):
        return redirect('/new')

    show = {
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }

    Show.save(show)
    return redirect('/dashboard')


@app.route('/edit/<int:show_id>')
def edit_show(show_id):
    if 'user_id' not in session:
        return redirect('/')

    show_to_edit = Show.get_one({'id': show_id})

    if not show_to_edit:
        return redirect('/dashboard')

    return render_template('edit_show.html', show=show_to_edit)

@app.route('/update/<int:show_id>', methods=['POST'])
def update_show(show_id):
    if 'user_id' not in session:
        return redirect('/')

    if not Show.validate_show(request.form):
        return redirect(f'/edit/{show_id}')

    data = {
        'id': show_id,
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'description': request.form['description']
    }

    Show.update_one(data)
    return redirect('/dashboard')

@app.route('/delete/<int:show_id>')
def delete_show(show_id):
    if 'user_id' not in session:
        return redirect('/')

    Show.delete({ 'id': show_id })
    return redirect('/dashboard')
