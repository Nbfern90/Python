from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import user
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')


@app.route("/users")
def users():
    # call the get all classmethod to get all users
    users = user.get_all()
    print(users)
    return render_template("users.html", users=user.get_all())


@app.route("/user/new")
def new_user():
    return render_template("new_user.html")


# relevant code snippet from server.py


@app.route('/user/create', methods=["POST"])
def create():
    user.save(request.form)
    return redirect('/users')

# USER PAGE


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user=user.get(data))

# EDIT PAGE


@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=user.get(data))


@app.route('/user/update', methods=["POST"])
def update():
    user.update(request.form)
    return redirect('/users')


@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    user.delete(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
