from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Greeting route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# About route
@app.route('/about')
def about():
    return "This is a Flask web application with enhanced styling."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
