# Import the Flask Class
from flask import Flask
from flask import request
import json
from csv_parser import get_genre

# Create an instance of Flask Class called name
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger the index() function
@app.route('/')
# The function returns the data in JSON format
def index():
    genre = request.args.get("genre")
    data = genre.title()
    result = get_genre(data)
    return json.dumps(result)

@app.route('/action')
def action():
    result = get_genre("Action")
    return json.dumps(result)
    
@app.route('/adventure')
def adventure():
    result = get_genre("Adventure")
    return json.dumps(result)

@app.route('/comedy')
def comedy():
    result = get_genre("Comedy")
    return json.dumps(result)

@app.route('/drama')
def drama():
    result = get_genre("Drama")
    return json.dumps(result)

@app.route('/romance')
def romance():
    result = get_genre("Romance")
    return json.dumps(result)


app.run('0.0.0.0', port=8080) # default Flask port is 5000, 8080 is used to be accessed externally

