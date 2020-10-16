import os

import time
from flask import Flask, render_template
from flask_pymongo import PyMongo


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_json('../application.config.json')
    mongo = PyMongo(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        user = mongo.db.user.find_one_or_404({'userName': 'maomishen'})
        print(user)	
        return str(user)

    @app.route('/xiaomi')
    def xiaomi():
        stime = time.time()
        ftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        mongo.db.xiaomi.insert({'time': stime, 'formatTime': ftime})
        return "success"

    @app.route('/list')
    def list():
        events = mongo.db.xiaomi.find({})
        return render_template('list.html',events=events)

    return app