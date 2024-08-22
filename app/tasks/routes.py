from flask import render_template, request, url_for, redirect, jsonify
from app.tasks import bp
from app.extensions import db
from app.models.task import Task
from app.models.tag import Tag

@bp.route('/', methods=('GET', 'POST'))
def index():
    tasks = Task.query.all()

    if request.method == 'POST':
        create_task()
    
    return render_template('tasks/index.html', tasks=tasks)

@bp.route('/<int:task_id>', methods=('PUT', 'PATCH'))
def updated_task(id):
    task_to_updated = Task.query.get_or_404(id)
    data = request.get_json()

    task_to_updated.title = data.get('title', task_to_updated.title)
    task_to_updated.content = data.get('content', task_to_updated.content)

    tag_ids = data.get('tag_ids', [])

    if tag_ids:
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        task_to_updated.tags = tags

    db.session.commit()

    return jsonify({'success': True, 'task': task_to_updated.to_dict()})


@bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('tasks.index'))


# --- Methodes ---

def create_task():
    new_task = Task(title=request.form['title'], content=request.form['content'])
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('tasks.index'))


