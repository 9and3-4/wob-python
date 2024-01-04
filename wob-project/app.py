from flask import Flask
from flask_apscheduler import APScheduler
from elasticsearch import Elasticsearch
from flask_cors import CORS
from routes.data import get_data
from routes.weather import get_weather, get_weather2
from routes.query import get_query
from routes.item import get_path_item
from routes.movie import get_movie
from routes.data_analysis import demo_graph, gender_data

import json

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=['http://localhost:3000'])

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()



app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
app.add_url_rule('/api/weather2', 'get_weather2', get_weather2, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)
