from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route to fetch random quote
@app.route('/get-quote')
def get_quote():
    response = requests.get("http://api.forismatic.com/api/1.0/", params={
        "method": "getQuote",
        "format": "json",
        "lang": "en"
    })
    quote = response.json()
    return jsonify({
        "content": quote["quoteText"],
        "author": quote["quoteAuthor"] or "Unknown"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
