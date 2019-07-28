from flask import Flask, request
from datetime import date
import requests
import urllib.request
import os
import random

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
    if data['text'] == '\luc':
        lucBot()
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
    sendMessage(daysSince)

def lucBot():
    number = random.uniform(1, 10)
    number
    if number <= 4:
        removeTom()
    elif number == 5:
        sendMessage('https://i.groupme.com/1080x1350.jpeg.c036fbed65a144b98320174c32eb73bf')
    elif number == 6:
        sendMessage('https://i.groupme.com/1080x1241.jpeg.eb9b0971005c4e1f89ea83808d26d278')
    elif number == 7:
        sendMessage('https://i.groupme.com/1080x1350.jpeg.ca6be17203af4796a43fa00b42f72c5d')
    elif number == 8:
        sendMessage('https://i.groupme.com/1080x1350.jpeg.b6be3125d82442f7b98fe80bf88da226')
    elif number == 9:
        sendMessage('https://i.groupme.com/1080x1350.jpeg.3a7249d893f44746aac47ccbe36ebb4c')
    elif number == 10:
        sendMessage('https://i.groupme.com/1080x1221.jpeg.64c1720db16f41d782848bc689bc8a80')

def sendMessage(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id'	: os.environ['thirtyTwoBotID'],
        'text'		: msg
    }
    response = requests.post(url, data=payload)
    return payload


