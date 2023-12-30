from flask import Flask
from flask import render_template, flash, request, url_for, redirect, session, jsonify
from flask_script import Manager
from app import app, migrate, MigrateCommand
from flask_cors import CORS, cross_origin


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

manager = Manager(app)
# manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    # manager.run()
