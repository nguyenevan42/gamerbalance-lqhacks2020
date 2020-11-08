from flask import Flask, render_template, current_app
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/gamelist.html')
def gamelist():
    return render_template('gamelist.html')

@app.route('/faq.html')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run()