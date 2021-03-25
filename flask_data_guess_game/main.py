import random
from flask import Flask, render_template, request, make_response, redirect, url_for
from models import User, db

app = Flask(__name__)
db.create_all()   # new tables in database


@app.route("/", methods=["GET"])
def index():
    email_address = request.cookies.get("email")

    if email_address:
        user = db.query(User).filter_by(email=email_address).first()
    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    secret_number = random.randint(1, 30)    # create a secret number

    user = db.query(User).filter_by(email=email).first()   # check if user already exists

    if not user:
        user = User(name=name, email=email, secret_number=secret_number)    # create u User object

        db.add(user)
        db.commit()   # save the user in the database

    response = make_response(redirect(url_for('index')))   # save user email into a cookie
    response.set_cookie("email", email)

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))

    email_address = request.cookies.get("email")

    user = db.query(User).filter_by(email=email_address).first()   # user from database / email address

    if guess == user.secret_number:
        message = f"You've guessed correctly! The secret number is str{guess}"

        new_secret = random.randint(1, 30)   # create a new secret number

        user.secret_number = new_secret   # update the secret number

        db.add(user)
        db.commit()   # update user object in database

    elif guess > user.secret_number:
        message = "Your guess is not correct... try something smaller!"
    elif guess < user.secret_number:
        message = "Your guess is not correct... try something bigger!"

    return render_template("result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
