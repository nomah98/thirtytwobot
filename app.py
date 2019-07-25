from flask import Flask, request

import urllib.request
import groupy
from groupy import Client
import groupy.api

app = Flask(__name__)

client = Client.from_token('RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h')

myGroups = client.groups.get('39105660')
members = myGroups.members()

@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    #print(data['members']['id'])
    #removeTom()
    for member in members:
        print("\"%s\",\"%s\"" % (member.id, member.nickname))
    return 'ok', 200


@app.route('/groups/39105660', methods=['GET'])
def groups():
    info = request.get_json()
    print(info)
    return info


#@app.route('/https://api.groupme.com/v3/groups/39105660/members/156400982779367387/remove?=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h', methods=['POST'])
def removeTom():
    #group.memberships.remove('156400982779367387')
    post_url = 'https://api.groupme.com/v3/groups/39105660/members/156406740175233974/remove?token=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h/'
    response = urllib.request.urlopen(post_url, {})
    return response