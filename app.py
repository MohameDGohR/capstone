import os
from flask import ( 
       Flask,
       request,
       abort,
       jsonify
 )
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from models import (setup_db,Movie,Actor)

from auth import (AuthError, requires_auth)





def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app,)

  @app.route('/')
  def get_greeting():
    excited = os.environ['EXCITED']
    greeting = "Hello"
    if excited == 'true': greeting = greeting + "!!!!!"
    return greeting
  @app.route('/movies/<int:movie_id>',methods=['PATCH'])
  @requires_auth('patch:movie')
  def update_movie(payload, movie_id):
        title = request.get_json().get('title')
        release_date = request.get_json().get('release_date')
        data =title or release_date
        if not data :
              abort(400) 
        movie = Movie.query.filter(Movie.id == movie_id).first()
        if not movie :
              abort(404) 
        try:
              if title:
                    movie.title = title 
              if release_date :
                    movie.release_date = release_date
              movie.update()
              return jsonify({
                    'success':True,
                    'movie':movie.format()
              }),200
        except:
              abort(422)







  @app.route('/actors/<int:actor_id>',methods=['PATCH'])
  @requires_auth('patch:actor')
  def update_actor(payload,actor_id):
        name = request.get_json().get('name')
        age = request.get_json().get('age')
        gender = request.get_json().get('gender')
        data = name or age or gender
        if not data :
              abort(400) 
        actor= Actor.query.filter(Actor.id == actor_id).first()
        if not actor :
              abort(404) 
        try:
              if name:
                    actor.name = name 
              if age :
                    actor.age = age 
              if gender :
                    actor.gender = gender 
              actor.update()
              return jsonify({
                    'success':True,
                    'actor':actor.format()
              }),200
        except:
              abort(422)


  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movie')
  def create_movie(payload):
         body = request.get_json()
         if not ('title' in body and 'release_date' in body  ):
               abort(422)
         new_title = body.get('title', None)
         new_release_date = body.get('release_date', None)
         try:
               movie = Movie(title=new_title, release_date=new_release_date)
               movie.insert()
               return jsonify({
                     'success': True,
                     'created': movie.id
                     })
         except:
               abort(422)



  @app.route('/actors',methods=['POST'])
  @requires_auth('post:actor')
  def create_actor(payload):
        body = request.get_json() 
        if not ('name' in body and 'age' in body and 'gender' in body  ):
              abort(422)
        name = body.get('name', None)
        age = body.get('age', None) 
        gender = body.get('gender', None)
        try:
              actor =  Actor(name=name,age=age,gender=gender)
              actor.insert()
              return jsonify({
                    'success':True,
                    'created': actor.id
                     })
        except:
              abort(422)



  @app.route('/actors/<int:actor_id>',methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor(payload,actor_id):
        try:
              actor =Actor.query.filter(Actor.id == actor_id).one_or_none()
              if actor is None :
                    abort(404)
              actor.delete()
              return jsonify({
                    'success':True,
                    'id':actor_id
                    })
        except:
              abort(422)
  @app.route('/movies/<int:movie_id>',methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(payload,movie_id):
        try:
              movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
              if movie is None :
                    abort(404)
              movie.delete()
              return jsonify({
                    'success':True,
                    'id':movie_id

              })
        except:
              abort(422)
                  

  @app.route('/actors',methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
        try:
              actors = list(map(Actor.format,Actor.query.all()))
              if actors is None :
                    abort(404)
              return jsonify({
                     'success':True,
                     'actors':actors
                     })
        except:
              abort(422)

  @app.route('/movies',methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
        try:
              movies= list(map(Movie.format,Movie.query.all()))
              if movies is None:
                    abort(404)
              return jsonify({
                    'success':True,
                     'movies':movies
              })
        except:
               abort(422)



 

  
  
  @app.after_request
  def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*") 
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
        return response

        
   
    
        
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404
  
  @app.errorhandler(401)
  def authentication_Error(error):
         return jsonify({
               "success": False, 
               "error": 401,
               "message": "unauthenticated  user  you must do login first"
               }), 401
  @app.errorhandler(403)
  def authentication_Error(error):
        return jsonify({
              "success": False, 
              "error": 403,
              "message": "you have not permisssion to do this action"
              }), 403




  @app.errorhandler(AuthError)
  def Authe_Error(error):
    #print(error)
    return jsonify({
        "success": False, 
        "error": error.error,
        "message": error.description
        }),error.status_code
   

 
  return app
  
  
  
  
app = create_app()
# run the app
if __name__ == '__main__':
      app.run()