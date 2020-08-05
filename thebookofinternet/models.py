import datetime
from thebookofinternet import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=True)
    post = db.Column(db.String(500), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return f'<Post {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'username': self.username,
            'post': self.post,
            'created_on': self.created_on
        }