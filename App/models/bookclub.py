from App.database import db
class BookClub(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(100), nullable=False)
  books = db.relationship('Book', backref='bookclub', lazy=True)
  users = db.relationship('User', backref='bookclub', lazy=True)

  def __init__(self, name, description):
    self.name = name,
    self.description = description

