from flask import render_template, request
from models import Person


def register_routes(app, db):

    @app.route("/", methods=["GET", "POST"])  # pyright: ignore
    def index():

        if request.method == "GET":
            people = Person.query.all()
            return render_template("index.html", people=people)

        elif request.method == "POST":
            name = request.form.get("name")
            age = int(request.form.get("age"))  # pyright: ignore
            job = request.form.get("job")

            person = Person(name=name, age=age, job=job)  # pyright: ignore

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template("index.html", people=people)

    @app.route("/delete/<pid>", methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()

        db.session.commit()

        people = Person.query.all()
        return render_template("index.html", people=people)

    @app.route("/details/<pid>")
    def detail(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template("detail.html", person=person)
