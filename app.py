from flask import Flask, request
from datetime import date

import urllib.request
import groupy
from groupy import Client
import groupy.api

app = Flask(__name__)



@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['text'] == '\larosa':
        larosaCounter()
    #print(data['members']['id'])
    removeTom()
    return 'ok'


@app.route('/groups/39105660', methods=['GET'])
def groups():
    info = request.get_json()
    print(info)
    return info


#@app.route('/https://api.groupme.com/v3/groups/39105660/members/156400982779367387/remove?=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h', methods=['POST'])
def removeTom():
    #group.memberships.remove('156400982779367387')
    post_url = 'https://api.groupme.com/v3/groups/39105660/members/459607275/remove?token=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h'
    response = urllib.request.urlopen(post_url, {})
    return response

def larosaCounter():
    death = date(2019, 3, 4)
    daysSince = death - date.today()
    print(daysSince)
    return daysSince
