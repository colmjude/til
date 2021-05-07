title: "SQLite db and flask"
tags: webdev, python, flask, development, sqlite, database
author: Colm Britton
--------------------

Steps to create and use an SQLite db with a flask app. Assumes using flask factory project structure.

Requirements:

    Flask-SQLAlchemy
    Flask-Migrate

Create models in `models.py`, e.g

    class Stock(db.Model):
        symbol = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(20), unique=False)
        created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(Stock, self).__init__(**kwargs)

    def __repr__(self):
        return '<Stock {} {}>'.format(self.symbol, self.name)

Point to sqlite db in `config.py`

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_ROOT, 'stocks.db')

In `extensions.py` add

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
    from flask_migrate import Migrate
    migrate = Migrate(db=db)

In `factory.py` add

    def register_extensions(app):
        from application.extensions import db, migrate
        db.init_app(app)
        migrate.init_app(app=app)

        # need this line for flask db migrate to find models
        from application import models

Create the migration repository (folder)

    flask db init

Create migrations -> do this each time you make a change to a model

    flask db migrate -m "change message"

Apply the changes with

    flask db upgrade


