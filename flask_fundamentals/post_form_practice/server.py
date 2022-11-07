
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "apples"

# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # Never render a template on a POST request/
    # Instead we will redirect to our index route
    return redirect('/success')
    # this stores the users submitted info


@app.route('/success')
def create_success():
    # this make sure the form is filled out
    if 'name' not in session:
        return redirect('/')
    return render_template('success.html')

# this is how to clear a session when it is over


# @app.route('/logout')
# def logout():
#     del session['name']
# or
# session.pop('email')

# this clears EVERYTHING from the session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
