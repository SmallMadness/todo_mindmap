from flask import render_template, request, url_for, redirect, jsonify
from app.tags import bp
from app.models.tag import Tag
from app.extensions import db
from app.extensions import db

@bp.route('/tags', methods=('GET', 'POST'))
def index():
    tags = Tag.query.all()

    if request.method == 'POST':
        new_tag = Tag(name=request.form['tag_name'])
        db.session.add(new_tag)
        db.session.commit()
        return redirect(url_for('tags.index'))
    
    return render_template('tags/index.html', tags=tags)

@bp.route('/tags/get', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    tags_list = [{"id": tag.id, "name": tag.name} for tag in tags]
    return jsonify(tags_list)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete_tag(id):
    tag_to_delete = Tag.query.get_or_404(id)
    db.session.delete(tag_to_delete)
    db.session.commit()
    return redirect(url_for('tags.index'))