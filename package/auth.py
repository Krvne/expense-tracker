from flask import Blueprint, render_template, redirect, flash, url_for
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
from datetime import datetime

now = datetime.now()

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    error = None
    if loginForm.validate_on_submit():
        # flash("{} successfully logged in!".format(loginForm.username.data))
        # session["username"] = loginForm.username.data

        # grab all data in form
        username = loginForm.username.data
        pwd = loginForm.password.data
        # try grab username from db
        u = User.query.filter_by(username=username).first()  # returns user obj or none
        if u is None:
            error = "Incorrect username or password."
        # if does exist compare passwords
        elif not check_password_hash(u.password, pwd):
            error = "Incorrect username or password."

        # passes match, login
        if error is None:
            # if error is none the user and pass are right
            login_user(u)
            flash("Sucessfully logged in {}.".format(username), "success")
            return redirect(url_for("main.home"))
        else:
            flash(error, "danger")

    return render_template("user.html", form=loginForm, heading="Login")


@bp.route("/register", methods=["GET", "POST"])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        # flash("{} successfully registered!".format(registerForm.username.data))
        # greb data from form
        username = registerForm.username.data
        email = registerForm.email.data
        pwd = registerForm.password.data
        # check if user already has name
        u = User.query.filter_by(username=username).first()  # returns user obj or none
        if u:
            flash("This username already exists, please login.", "info")
            return redirect(url_for("auth.login"))

        # if username is unique crete user and commit
        pwd_hash = generate_password_hash(pwd)
        new_user = User(
            username=username,
            email=email,
            password=pwd_hash,
        )
        db.session.add(new_user)
        db.session.commit()
        flash(
            "Sucessfully registered {}. You may now login.".format(username), "success"
        )
        return redirect(url_for("auth.login"))

    else:
        return render_template("user.html", form=registerForm, heading="Register")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Successfully logged out!", "success")
    return redirect(url_for("auth.login"))
