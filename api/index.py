from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World hey hey!'

@app.route('/about')
def about():
    return 'About (nice, you did it!)'
