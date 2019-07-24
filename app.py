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


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    removeTom()
    return 'rwarawrd'


def removeTom():
    group.memberships.remove('156400982779367387')
