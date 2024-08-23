from flask_login import UserMixin  # pyright: ignore
from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __repr__(self) -> str:
        return f"<User: {self.username}, Role: {self.role}>"

    def get_id(self):
        return self.uid
