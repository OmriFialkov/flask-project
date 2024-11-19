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
    api_url = "https://api.quotable.io/random"
    response = requests.get(api_url)

    # Check for errors in the API request
    if response.status_code == 200:
        quote = response.json()
        return jsonify(quote)  # Return the quote as JSON
    else:
        return jsonify({"content": "Error fetching quote", "author": "Unknown"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
