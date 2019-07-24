

from flask import Flask, request
import groupy
from groupy import Client, api
from groupy.api import messages


token = 'RFB9t35ct1lA7wHOdbBNZpJKeEqiDTPCGz5nwN5h'
group = Client.from_token(token).groups.get('39105660')
groupMembers = group.members()


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
    group.remove(71126415)
   # messages = group.messages()
   # msg = messages.newest
  #  if msg.user_id == 32941054:




