from flask_wtf import FlaskForm
from wtforms.widgets.core import CheckboxInput, Input
from wtforms.fields.core import BooleanField
from wtforms import (
    TextAreaField,
    SubmitField,
    StringField,
    PasswordField,
    SelectField,
    DateField,
    DecimalField,
    IntegerField,
)
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    NumberRange,
    Length,
    ValidationError,
    DataRequired,
)


###  AUTH FORMS  ###
class LoginForm(FlaskForm):
    username = StringField(
        "Enter your username:",
        validators=[InputRequired(message="Username is required.")],
    )
    password = PasswordField(
        "Enter your password:",
        validators=[InputRequired(message="Passowrd is rewuired.")],
    )
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField(
        "Enter your username:",
        validators=[InputRequired(message="Username is required.")],
    )
    email = StringField(
        "Enter your email:",
        validators=[
            InputRequired("An email address is required."),
            Email("Please enter a valid email address."),
        ],
    )
    password = PasswordField(
        "Enter your password:",
        validators=[
            EqualTo("confirm", message="Passwords dont match."),
            InputRequired(message="Passowrd is rewuired"),
        ],
    )
    confirm = PasswordField(
        "Confirm your password:",
        validators=[InputRequired(message="Passowrd is rewuired")],
    )
    submit = SubmitField("Register")
