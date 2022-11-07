from flask import Flask, render_template, request, redirect
# import the class from peeps.py
from peeps import Peeps

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/read')


@app.route('/read')
def read():
    return render_template("read.html", people=Peeps.get_all())


@app.route('/peep/create')
def create():
    return render_template("create.html")


@app.route('/peep/create', methods=['POST'])
def create_peep():

    print(request.form)
    Peeps.save(request.form)
    return redirect('/read')


@app.route('/peep/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit.html", person=Peeps.get_one(data))


@app.route('/peep/edit', methods=['POST'])
def update():

    Peeps.edit(request.form)
    return redirect('/read')


@app.route('/peep/delete/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Peeps.delete(data)
    return redirect('/read')


@app.route('/peep/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show.html", person=Peeps.get_one(data))


if __name__ == "__main__":
    app.run(debug=True)
