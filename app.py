import requests
import os
import json
import queue
from flask import Flask, request
from groupy import Client
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from collections import OrderedDict

client = Client.from_token('3cefe43bef5d04bd22d3958597')

app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
	print('JuliaPakey')
	return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
   # removeLuc()
    sent = str(data['text'])
    print(client.group.members)
    return data['user_id']

#def removeLuc(data):
#    if data['id'] == '32941054':


