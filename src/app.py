__author__= 'kalamitis'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_method():
    return "Hello, world!"

if __name__ == '__main__':
    app.run()