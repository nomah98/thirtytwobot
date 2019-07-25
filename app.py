from flask import Flask, request, Response

import urllib.request
import groupy
from groupy import Client, api


client = Client.from_token('RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h')

group = client.groups.get('39105660')

app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey 2')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['DELETE'])
def webhook():
    data = request.get_json()
    #group.memberships.remove('156400982779367387')
    removeTom()
    return 'ok', 200

#@app.route('/https://api.groupme.com/v3/groups/39105660/members/156400982779367387/remove?=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h', methods=['POST'])
def removeTom():
    #group.memberships.remove('156400982779367387')
    post_url = 'https://api.groupme.com/v3/groups/39105660/members/156400982779367387/remove?token=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h'
    response = urllib.request.urlopen(post_url, {})
    return 'ok'