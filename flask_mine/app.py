from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!!!"

@app.route("/meme")
def random_meme():
    # Make the API request
    response = requests.get("https://api.imgflip.com/get_memes")

    # Parse the JSON data
    data = response.json()

    # Extract the list of memes (if available)
    memes = data.get('data', {}).get('memes', [])

    # Select a random meme or use a placeholder if no memes are found
    if memes:
        random_meme = random.choice(memes)['url']
    else:
        random_meme = "https://via.placeholder.com/300?text=No+Meme+Found"

    # Render the template with the selected meme
    return render_template('random_meme.html', meme=random_meme)



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
