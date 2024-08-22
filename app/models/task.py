from app.extensions import db
from app.associations import task_tags

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    task_list_id = db.Column(db.Integer, db.ForeignKey('task_lists.id'))
    task_list = db.relationship("Task_List", back_populates="tasks")

    tags = db.relationship('Tag', secondary=task_tags, back_populates='tasks')

    def __repr__(self):
        return f'<Task "{self.title}">'
