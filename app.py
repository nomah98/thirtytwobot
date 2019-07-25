from flask import Flask, request

import urllib.request

app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
    print('JuliaPakey')
    return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data['members']['id'])
    removeTom()
    return 'ok', 200


@app.route('/groups/39105660', methods=['GET'])
def groups():
    info = request.get_json()
    print(info)
    return 'ok'


#@app.route('/https://api.groupme.com/v3/groups/39105660/members/156400982779367387/remove?=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h', methods=['POST'])
def removeTom():
    #group.memberships.remove('156400982779367387')
    post_url = 'https://api.groupme.com/v3/groups/39105660/members/156406740175233974/remove?token=RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h/'
    response = urllib.request.urlopen(post_url, {})
    return response