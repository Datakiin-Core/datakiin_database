"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(FlaskForm):
    """User Sign-up Form."""
    user_name = StringField("Name", validators=[DataRequired()])
    user_email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    user_password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters long."),
            validators.Regexp(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
            message="Password must include at least 1 uppercase," +
                    "1 lowercase, 1 number, and 1 special character."
        )
        ],
    )
    user_password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("user_password", message="Passwords must match."),
        ],
    )
    user_metadata_website = StringField("Website", validators=[Optional()])
    submit_button = SubmitField("Register")

class UpdateForm(FlaskForm):
    """User Update Form."""

    old_user_password = PasswordField("Old Password", validators=[DataRequired()])

    user_password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=12, message="Password must be at least 12 characters long."),
            validators.Regexp(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
            message="Password must include at least 1 uppercase," +
                    "1 lowercase, 1 number, and 1 special character."
        )
        ],
    )
    user_password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("user_password", message="Passwords must match."),
        ],
    )
    submit_button = SubmitField("Change Password")

class LoginForm(FlaskForm):
    """User Log-in Form for existing users."""
    user_email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Enter a valid email.")
        ]
    )
    user_password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField("Log In")
