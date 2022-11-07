from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<string>')
def say(string):
    return "hi " + string


@app.route('/say/<string:banana>/<int:num>')
def hello(banana, num):
    return render_template("hello.html", banana=banana, num=num)


@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output


@app.route('/play/<int:num>/<string:color>')
def play(num, color):

    return render_template('hello.html', num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
