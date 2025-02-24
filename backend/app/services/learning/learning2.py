from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {escape(name)}!'

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)