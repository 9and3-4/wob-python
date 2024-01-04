from flask import Flask
from flask_apscheduler import APScheduler
from elasticsearch import Elasticsearch
from flask_cors import CORS
from routes.weather import get_weather, get_weather2



import json

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=['http://localhost:8111'])

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()



app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
app.add_url_rule('/api/weather2', 'get_weather2', get_weather2, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)
