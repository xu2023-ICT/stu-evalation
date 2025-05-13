from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    db.init_app(app)

    from .routes import submission, rating, teacher
    app.register_blueprint(submission.bp)
    app.register_blueprint(rating.bp)
    app.register_blueprint(teacher.bp)

    return app
