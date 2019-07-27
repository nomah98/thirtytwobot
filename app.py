from flask import Flask, request
from datetime import date
import requests
import urllib.request
import os
import groupy
from groupy import Client
import groupy.api

app = Flask(__name__)
app.config['apiToken'] = os.environ['apiToken']
app.config['thirtyTwoBotID'] = os.environ['thirtyTwoBotID']


@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['text'] == '\larosa':
        larosaCounter()
    if data['user_id'] == '36815098':
        removeTom()
    return 'ok'


@app.route('/groups/39105660', methods=['GET'])
def groups():
    info = request.get_json()
    print(info)
    return info

def removeTom():
    post_url = 'https://api.groupme.com/v3/groups/39105660/members/459607275/remove?token=' + os.environ['apiToken']
    response = urllib.request.urlopen(post_url, {})
    return response

def larosaCounter():
    death = date(2019, 3, 4)
    daysSince = str((date.today() - death).days) + ' days since Larosa died'
    print(daysSince)
    sendMessage(daysSince)
    return daysSince


def sendMessage(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id'	: os.environ['thirtyTwoBotID'],
        'text'		: msg
    }
    response = requests.post(url, data=payload)
    return payload
