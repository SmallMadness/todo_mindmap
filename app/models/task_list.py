from app.extensions import db

class Task_List(db.Model):
    __tablename__ = "task_lists"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    
    tasks = db.relationship('Task', back_populates='task_list', lazy='dynamic')

    def __repr__(self):
        return f'<Task List {self.title}>'