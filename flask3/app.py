from flask import Flask, render_template
import requests
from flask import jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!!!"

@app.route('/greet/<person>')
def greet(name):
    return render_template('greet.html', person=name)


@app.route("/nba/stats")
def get_nba():
    
    api_url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
    
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    data=response.json()

    return data


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)