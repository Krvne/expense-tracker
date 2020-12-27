from flask import Blueprint, render_template, redirect, flash, url_for

# from .forms import
# from .models import
from . import db
from datetime import datetime

now = datetime.now()

# file blueprint. Use to reffer to functions in url_for functions
# url_for('main.FUNCTION_NAME')
bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
