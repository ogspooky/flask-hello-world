from flask import Flask
from flask import render_template, request
import requests
import re
import json
import logging

API_KEY = '3c19fe27-82b3-40dc-beae-606d545ea943'
BASE_URL='https://api.hypixel.net/v2/'

app = Flask(__name__, template_folder='../templates')


@app.before_request
def validate_api_key():
    url = BASE_URL + f"?key={API_KEY}" 
    response = requests.get(url)
    data = json.loads(response.text)
    if data['success'] == False:
        if data['cause'] == 'Invalid API key':
            app.logger.error('Invalid API Key')
            return 'Invalid API Key', 401
        return 'Unknown error', 500
    return None, 200


def is_player_online(player_name=None):
    # query api with UUID
    uuid = get_uuid(player_name)
    url = BASE_URL + f"status?key={API_KEY}&uuid={uuid}"
    response = requests.get(url)
    data = json.loads(response.text)
    app.logger.debug(data)
    return data['session']['online']

@app.route('/')
def home():
    return 'Hello, gamer-word!'

@app.route('/input', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        result = is_player_online(request.form['player_name'])
        return str(result)

    return render_template('index.html')

def get_uuid(player_name=None):
    url = f"https://playerdb.co/api/player/minecraft/{player_name}"
    response = requests.get(url)
    data = json.loads(response.text)
    uuid = data['data']['player']['id']
    return uuid


def get_player_last_played(player_name=None):
    uuid = get_uuid(player_name)
    url = BASE_URL + f"recentgames?key={API_KEY}&uuid={uuid}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['session']['lastLogin']

    


    
    
if __name__ == '__main__':
    # print(is_player_online('Yhuvko'))
    print(get_player_last_played('Yhuvko'))