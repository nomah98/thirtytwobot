import requests
import os
import json
import queue
from flask import Flask, request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from collections import OrderedDict

app = Flask(__name__)


@app.route('/thirtytwobot', methods=['GET'])
def index():
	print('JuliaPakey')
	return 'https://www.instagram.com/p/BJmB0B4gLQO/'


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    sent = str(data['text'])
    print(data['user_id'])
    return data['user_id']
