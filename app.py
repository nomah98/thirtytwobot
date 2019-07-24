

from flask import Flask, request
import groupy
from groupy import Client
import groupy.api

token = 'RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h'
group = Client.from_token(token).groups.get('39105660')


app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
	print('JuliaPakey')
	return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
   # sent = str(data['text'])
 #   print(groupy.Client.groups
    for i in group.members:
        print(i)
    return data['user_id']




