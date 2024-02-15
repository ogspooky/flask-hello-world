from flask import Flask
from flask import render_template, request, render_template_string
import requests
import re
import json

API_KEY = '3c19fe27-82b3-40dc-beae-606d545ea943'
BASE_URL='https://api.hypixel.net/v2/'

app = Flask(__name__)




def is_player_online(player_name=None):
    # query api with UUID
    uuid = get_uuid(player_name)
    url = BASE_URL + f"status?key={API_KEY}&uuid={uuid}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['session']['online']

@app.route('/')
def home():
    return 'Hello, gamer-word!'

@app.route('/input', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        result = is_player_online(request.form['player_name'])
        return str(result)
    # render the generic empty input box
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Input Box Example</title>
        </head>
        <body>
            <form method="post">
                <input type="text" name="player_name" placeholder="Enter player name">
                <input type="submit" value="Check Status">
            </form>
        </body>
        </html>
    """

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