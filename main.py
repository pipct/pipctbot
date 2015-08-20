from flask import Flask, request
import urllib
import urllib2
import json
import logging
app = Flask(__name__)
app.config['DEBUG'] = True

with open('config.json') as config:
    config = json.load(config)

bot_id = config["bot_id"]


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/' + bot_id, methods=['POST'])
def getUpdates():
    content = request.json
    if 'text' in content['message']:
        reply = {
            "chat_id": content['message']['chat']['id'],
            "text": content['message']['text']
            }
        logging.debug(content)
        result = urllib2.urlopen("https://api.telegram.org/bot" +
                                 bot_id + "/sendMessage",
                                 urllib.urlencode(reply)).read()
        logging.debug(result)
    return 'Message Recieved!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Nothing to see, please go away.', 404