from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    Bootstrap(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    from app.task_lists import bp as task_lists_bp
    app.register_blueprint(task_lists_bp, url_prefix='/task_lists')

    from app.tags import bp as tags_bp
    app.register_blueprint(tags_bp, url_prefix='/tags')

    return app