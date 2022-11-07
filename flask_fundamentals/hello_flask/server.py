from flask import Flask, render_template
app = Flask(__name__)


@app.route('/coding')
def coding_is_fun():
    return "Coding is so fun!"




@app.route('/hello/<int:num>/<string:word>')
def template_hello(num, word):
    return render_template('hello.html', num=num, word=word)


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0, num):
        output += f"<p>{word}</p>"

    return output


@app.route('/user/<string:user_name>/<int:user_age>')
def user_info(user_age, user_name):
    # return f"Hello {user_name}, you are {user_age} years old."
    return render_template('dynamic.html', name=user_name, age=user_age)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":
    app.run(debug=True)
