"""DATABASE MODELS """
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
#pylint: disable=R0903
class Image(db.Model):
    """ USER IMAGES DATABASE MODEL """
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('flasksession-users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)

class User(UserMixin, db.Model):
    """ USER ACCOUNT DATABASE MODEL """

    __tablename__ = "flasksession-users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def set_password(self, password):
        """ HASH PASSWORDS """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """ CHECK PASSWORDS """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id}, name={self.name},"\
               f"email={self.email}, password={self.password}>"

    def get_images(self):
        """ Return images associated with the user """
        return Image.query.filter_by(user_id=self.id).all()

    def add_image(self, filename):
        """ Add a new image for the user """
        new_image = Image(user_id=self.id, filename=filename)
        db.session.add(new_image)
        db.session.commit()

class Message(db.Model):
    """ ERROR LOGS DATABASE MODEL """
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, content):
        self.content = content
