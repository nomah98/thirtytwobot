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
    if data['text'] == 'luc':
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
    url = 'https://api.instagram.com/oauth/access_token'
    payload = {
    'client_id': 'fd94c8a2662e472aa3b203184e915ec6',
    'client_secret': '4271ddc1006b48d19e14a4419a8f773a',
    'grant_type' : 'authorization_code',
    'redirect_uri' : 'https://glacial-garden-64910.herokuapp.com/',
    'code' : '10616b10653947238878e74ced4b4b74'
    }
    response = requests.post(url, data=payload)
    print(payload)
    return payload


def sendMessage(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id'	: os.environ['thirtyTwoBotID'],
        'text'		: msg
    }
    response = requests.post(url, data=payload)
    return payload
