from flask import Flask, request
from datetime import date
import requests
import urllib.request
import os
import random
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import sql

app = Flask(__name__)
app.config['apiToken'] = os.environ['apiToken']
app.config['thirtyTwoBotID'] = os.environ['thirtyTwoBotID']
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import tables
from tables import Roommate, Insult


@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    sentMessage = data['text'].split(' ')
    command = sentMessage[0]
    if command == '\larosa':
        larosaCounter()
    if data['user_id'] == '36815098':
        removeTom()
    if command == '\luc':
        lucBot()
    if command == '\d':
        urban(sentMessage[2:])
    if command == '\\roast':
        roastBot(sentMessage)
    if command == '\\addroast':
        addRoast(sentMessage)
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
    number = random.randrange(11)
    print(number)
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


def urban(term):
    r = requests.get("https://mashape-community-urban-dictionary.p.rapidapi.com/define?term=" + term,
                     headers={
                         "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
                         "X-RapidAPI-Key": "b3ca2c3c98msh50b2e8571820722p108617jsn5157c02d70c6"
                     }
                     )
    definition = 'Definition: ' + r.json()['list'][0]['definition'] + '\n'
    ex = '\n Example: ' + r.json()['list'][0]['example']
    defex = definition + ex
    defexclean = defex.replace("[", "")
    defexclener = defexclean.replace("]", "")
    sendMessage(defexclener)


def roastBot(message):
    roastee = message[1]
    resDirty = Insult.query.filter_by(name=roastee).first()
    res = str(resDirty)
    resClean = res.replace("<", "")
    resCleaner = resClean.replace(">", "")
    insultMessage = resCleaner.split(' ')
    sendMessage(insultMessage[1:])


def addRoast(message):
    print(message)




