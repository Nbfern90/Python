from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "apples"


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
