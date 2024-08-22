from flask import render_template, request, url_for, redirect
from app.task_lists import bp
from app.models.task_list import Task_List
from app.extensions import db
from app.extensions import db

@bp.route('/', methods=('GET', 'POST'))
def index():
    task_lists = Task_List.query.all()

    if request.method == 'POST':
        new_task_list = Task_List(title=request.form['title'])
        db.session.add(new_task_list)
        db.session.commit()
        return redirect(url_for('task_lists.index'))
        
    return render_template('task_lists/index.html', task_lists=task_lists )