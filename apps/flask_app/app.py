# This project demos how to setup a system test
# for a simple flask app

from flask import Flask, jsonify

# create a flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, world!'})  # return msg as json string


if __name__ == '__main__':
    app.run()
