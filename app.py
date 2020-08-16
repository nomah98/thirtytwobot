from flask import Flask, request
from datetime import date
import requests
import urllib.request
import os
import random
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import sql
from groupy.api import groups
from groupy.api.attachments import Mentions

app = Flask(__name__)
app.config['apiToken'] = os.environ['apiToken']
app.config['thirtyTwoBotID'] = os.environ['thirtyTwoBotID']

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
    if data['user_id'] == '32941054':
        lucBot()
    if command == '\d':
        define = " ".join(sentMessage[1:])
        urban(define)
    if command == '\\roast':
        roastBot2(sentMessage)
    if command == '\\addroast':
        addRoast(sentMessage)
    if command == '\\addroastee':
        addRoastee(sentMessage)
    if command == '\\trash':
        pickRoommate()
    return 'ok'


def removeLuc():
    post_url = 'https://api.groupme.com/v3/groups/49060077/members/428245754/remove?token=' + os.environ['apiToken']
    response = urllib.request.urlopen(post_url, {})
    return response


def larosaCounter():
    death = date(2019, 3, 4)
    daysSince = str((date.today() - death).days) + ' days since we moved in'
    sendMessage(daysSince)


def lucBot():
    number = random.randint(1, 200)
    if number <= 3:
        removeLuc()
    return number


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


def roastBot2(message):
    roastee = message[1]
    nameList = []
    for nm in db.session.query(Roommate).filter_by(name=roastee):
        nameList.append(nm)
    if len(nameList) != 1:
        sendMessage(roastee + ' is not in the database')
    else:
        insultList = []
        for ins in db.session.query(Insult).filter_by(name=roastee):
            insultList.append(ins)
        number = random.randrange(len(insultList))
        insult = insultList[number]
        res = str(insult)
        resClean = res.replace("<", "")
        resCleaner = resClean.replace(">", "")
        insultMessage = resCleaner.replace("Insult ", "")
        sendMessage(insultMessage)


def addRoast(message):
    roastee = str(message[1])
    roastArr = message[2:]
    roastString = " ".join(roastArr)
    newInsult = Insult(roastee, roastString)
    db.session.add(newInsult)
    db.session.flush()
    db.session.commit()


def addRoastee(message):
    roastee = str(message[1])
    newRoommatee = Roommate(roastee)
    db.session.add(newRoommatee)
    db.session.flush()
    db.session.commit()

def pickRoommate():
    r = requests.get('https://api.groupme.com/v3/groups/49060077?token=' + os.environ['apiToken'])
    q = r.json()
    memberDict = { }
    for i in q['response']['members']:
        memberDict[str(i['user_id'])] = str(i['name'])
    selectionID = random.choice(list(memberDict.keys()))
    nickname = memberDict.get(selectionID)
    sendRoomie(selectionID, nickname)


def sendRoomie(ID, name):
    url = 'https://api.groupme.com/v3/bots/post?token=' + os.environ['apiToken']
    nameLength = len(name) + 1
    payload = {
        'bot_id' : os.environ['thirtyTwoBotID'],
        'text' : 'It is @' + name + 's turn to take out the trash tonight',
        'attachments' : [
            {
                'type': 'mentions',
                'loci': [[5, nameLength]],
                'user_ids': [ID]
            }
        ]
            #[{"loci": [[3, 5]], "type": "mentions", "user_ids": ["37983222"]}],

    }
    response = requests.post(url, json=payload)
    return payload






