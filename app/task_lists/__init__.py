from flask import Blueprint

bp = Blueprint('task_lists', __name__)

from app.task_lists import routes