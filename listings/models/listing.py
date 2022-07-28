from ..database.db import db

class Listing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(500))
    email = db.Column(db.String(500))
