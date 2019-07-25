from flask import Flask, request
import groupy
from groupy import Client, api
import groupy.api.groups
import groupy.api.messages
import groupy.api.memberships

client = Client.from_token('RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h')

group = client.groups.get('39105660')

app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey 2')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST', 'GET'])
def webhook():
    data = request.get_json()
    group.memberships.remove(data['id'])
    removeTom()
    return 'OK'

@app.route('/groups/39105660/members/156400982779367387/remove', methods=['POST'])
def removeTom():
    group.memberships.remove('156400982779367387')
    return 'OK'