# Full Stack Movie Actor Backend
## Introduction 

This project is to provide information about actors and movies.
I developed this project to make use of the knowledge I acquired in this nanodegree and hence gain confidence in these skills.
Our application API is hosted live via Herok with url : https://moviesactors2020.herokuapp.com/
## Getting Started

### Installing Dependencies


#### Python 3.7+

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Database Setup
With Postgres running, restore a database using the movie_actor.psql file provided. From the backend folder in terminal run:
```bash
psql movie_actor < movie_actor.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server for Linux  execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
To run the server for Windows  execute:

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```


ENVIRONMENt Variable for project will  be found at file setup.sh

## Database 

There are total 3 data tables in this projectL Movie and Actor and Movie_Actor .

To setup the database, run:
```
dropdb movie_actor
run command flask db init
flask db migration 
flask db upgrad

psql movie_actor < movie_actor.psql  
```
## Endpoints 

There are total 8 endpoints in this projects: 
### GET '/actors' 
    Returns a List of all actors.
    Sample curl:
      curl --location --request GET 'https://moviesactors2020.herokuapp.com/actors' \
       --header 'Authorization: Bearer  Jwt '
    Sample response output:
    {
    "actors": [
        {
            "age": 55,
            "gender": "male",
            "id": 1,
            "name": "Bill paxton"
        },
        {
            "age": 44,
            "gender": "male",
            "id": 2,
            "name": "van desil"
        }
    ],
    "success": true }


###  GET '/movies'
     Returns a List of all movies.
     Sample curl:
        curl --location --request GET 'https://moviesactors2020.herokuapp.com/movies' \
        --header 'Authorization: Bearer Jwt'
        Sample response output:
        {
          "movies": [
            {
               "id": 1,
               "release_date": "Fri, 25 Nov 
                 2005    00:00:00 GMT",
               "title": "home alone1"
           },
           {
                "id": 2,
                "release_date": "Thu, 25 Nov 
                  1999  00:00:00 GMT",
                "title": "home alone2"
           }
                  ],
          "success": true }

 

### DELETE '/actors/id'
    Delete an  actor with specified id and returns id of actor that was deleted.
    Sample curl :
      curl --location --request DELETE 'https://moviesactors2020.herokuapp.com/actors/5' \
      --header 'Authorization: Bearer Jwt'
      Sample response output:
        {
          "id": 5,
          "success": true }

    
### DELETE '/movies/id'
    Delete an  movie with specified id and returns id of movie that was deleted.
    Sample curl :
        curl --location --request DELETE  'https://moviesactors2020.herokuapp.com/movies/6'\
        --header 'Authorization: Bearer Jwt'
    Sample response output:
        {
            "id": 6,
            "success": true }

### POST '/actors'
    Add a new actor to Actors table in the database   and returns id of actor  that was created.
    Sample curl :
        curl --location --request POST 'https://moviesactors2020.herokuapp.com/actors' \
        --header 'Authorization: Bearer Jwt' \
        --header 'Content-Type: application/json' \
        --data-raw ' {
               "age": 45,
               "gender": "female",
          
               "name": "Itziar Ituño Martínez "
            }'
    Sample response output:
        {
            "created": 6,
            "success": true }


###  POST '/movies'
    Add a new movie to Movies table in the database   and returns id of movie  that was created.
    Sample curl:
        curl --location --request POST 'https://moviesactors2020.herokuapp.com/movies' \
        --header 'Authorization: Bearer Jwt ' \
        --header 'Content-Type: application/json' \
        --data-raw '{
             "title":"La casa de papel 2",
             "release_date":"10/16/2017"}'
    Sample response output:
        {
              "created": 7,
              "success": true }


###  PATCH  '/actors/id'
    Update an actor with spicifed id and returns actor that was updated.
    Sample curl:
        curl --location --request PATCH 'https://moviesactors2020.herokuapp.com/actors/6' \
        --header 'Authorization: Bearer Jwt ' \
        --header 'Content-Type: application/json' \
        --data-raw ' {
            "age": 46,
            "gender": "female",
          
            "name": "Itziar Ituño Martínez "
            }'
    Sample response output:
        {
             "actor": {
             "age": 46,
             "gender": "female",
             "id": 6,
             "name": "Itziar Ituño Martínez "
        },
        "success": true }

### PATCH '/movies/'
    Update an movie with spicifed id and returns movie that was updated.
    Sample curl:
         curl --location --request PATCH 'https://moviesactors2020.herokuapp.com/movies/7' \
         --header 'Authorization: Bearer Jwt' \
         --header 'Content-Type: application/json' \
         --data-raw '{
                 "title":"La casa de papel 2",
                 "release_date":"10/17/2017"}'
    Sample response output:
           {
           "movie": {
           "id": 7,
           "release_date": "Tue, 17 Oct 2017 00:00:00 
            GMT",
           "title": "La casa de papel 2"
            },
            "success": true}


## Roles

There are 3 roles in the project: Casting Assisnt, Casting Director, and Exectuive Producer 

Here is the permission table for each role: 

Casting Assistant: 
1. GET /actors
2. GET /movies 

Casting Director: 
1. GET /actors
2. GET /movies
3. DELETE /actors/
5. POST /actors/
7. PATCH  /actors/
8. PATCH /actors/

Exectuive Producer:
1. GET /actors
2. GET /movies
3. DELETE /actors/
4. DELETE /movies/
5. POST /actors/
6. POST/movies/
7. PATCH  /actors/
8. PATCH /actors/


## Testing
To run the tests, run

```
bash recreate_movie_test_sql  
python test_app.py
```



