from app.extensions import db
from app.associations import task_tags

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    tasks = db.relationship('Task', secondary=task_tags, back_populates='tags')

    def __repr__(self):
        return f'<Tag {self.name}>'