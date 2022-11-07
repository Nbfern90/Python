from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def say(name):
    return f"Greetings {name} !"


@app.route('/<int:num>/<string:word>')
def repeat(num, word):
    rep_num = ''

    for i in range(0, num):
        rep_num += (f"{word}")
        return rep_num


if __name__ == "__main__":
    app.run(debug=True)
