from App.database import db
class Book(db.Model):
  book_id = db.Column(db.String, primary_key=True)
  Title = db.Column(db.String(100), nullable=False)
  Author = db.Column(db.String(100), nullable=False)
  Publication_Year = db.Column(db.Integer, nullable=False)
  status = db.Column(db.String(100), nullable=False)
  image = db.Column(db.String(100))
  
  def __init__(self, book_id,Title, Author, Publication_Year, status,image):
    self.book_id =book_id
    self.Title = Title
    self.Author = Author
    self.Publication_Year = Publication_Year
    self.status = status
    self.image = image
    

  def to_dict(self):
    return{
      'book_id': self.book_id,
      'Title': self.Title,
      'Author': self.Author,
      'Publication_Year': self.Publication_Year,
      'status': self.status,
      'image': self.image
    }
    