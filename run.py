from flask import Flask
from flask import render_template, flash, request, url_for, redirect, session, jsonify
# from flask_script import Manager
from app import app

# manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    # manager.run()