#! /usr/bin/python3
# This is the main file where everything will be handled
from flask import Flask, render_template, request, url_for, redirect
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       username = request.form['name']
       return render_template('test.html', name=username)
    else:
        return render_template('index.html')

@app.route('/test')
def testing():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
