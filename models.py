import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, String, Integer, create_engine,ForeignKey
import json




#database_name =   "trivia"
#database_path = "postgresql://postgres:123456@{}/{}".format('localhost:5432', database_name)
database_path = os.environ.get('HEROKU_POSTGRESQL_PUCE_URL')

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

Movie_Actor = db.Table('Movie_Actor', db.Model.metadata,
    db.Column('Movies_id', db.Integer, db.ForeignKey('Movies.id')),
    db.Column('Actors_id', db.Integer, db.ForeignKey('Actors.id'))
)


class MovieActorcomon(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Movie(MovieActorcomon):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key=True)
    # String Title
    title = Column(String, nullable=False)
    release_date = Column(db.Date)

    children = db.relationship("Actor",
                    secondary=Movie_Actor)
    def __int__(self, title, release_date):
        self.title = title
        self.release_date = release_date
    
    def format(self):
          return {
            'id':self.id,
            'title':self.title,
            'release_date':self.release_date
          }
class Actor(MovieActorcomon):
    __tablename__ = 'Actors'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    age = db.Column(Integer)
    gender = db.Column(String)
    movies = db.relationship("Movie",
                    secondary=Movie_Actor)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    
    def format(self):
          return {
            'id':self.id,
            'name':self.name,
            'gender':self.gender,
            'age':self.age
            }
