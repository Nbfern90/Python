from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "apples"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/submit')


@app.route('/submit')
def create_success():

    if 'name' not in session:
        return redirect('/')
    return render_template('submit.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
