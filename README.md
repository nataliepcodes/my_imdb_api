# Welcome to My Imdb Api
***

## Task
_What is the problem? And where is the challenge?_\
Create a backed app with a light framework.\
It will receive a requested Genre and only serve Movies with the corresponding Genre.\
All routes to return a JSON format


## Description
_How have you solved the problem?_\
Used Flask framework, csv parser function to read the csv file. 

## Installation
_How to install your project? npm install? make? make re?_
```
pip install Flask
```
Then run the server with:
```
python app.py
```

## Usage
_How does it work?_\
Six Genres can be accessed with this application:
* genre with an argument, e.g. Action, Comedy
* Action
* Adventure
* Comedy
* Drama
* Romance\
GET on / This route will parse the GET parameter genre, to be able to filter by movie genre.
Example on how to access this route:
```
curl "http://localhost:8080?genre=action"
```
GET on /action This route will only serve action movies.
Example on how to access this route:
```
curl "http://localhost:8080/action"
```

### The Core Team
Natalie P.

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt="Qwasar SV -- Software Engineering School's Logo" src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
