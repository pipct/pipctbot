from flask import Flask, request
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json
import logging
main = application = app = Flask(__name__)
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
    logging.debug(content)
    if 'title' not in content['message']['chat']:
        if 'text' in content['message']:
            reply = {
                "chat_id": content['message']['chat']['id'],
                "text": content['message']['text']
                }
            result = urllib.request.urlopen("https://api.telegram.org/bot" +
                                     bot_id + "/sendMessage",
                                     urllib.parse.urlencode(reply)).read()
            logging.debug(result)
    if 'voice' in content['message']:
        reply = {
            "chat_id": content['message']['from']['id'],
            "text": "Please don't use voice messages, or we will find you and we will kill you!"
            }
        result = urllib.request.urlopen("https://api.telegram.org/bot" +
                                 bot_id + "/sendMessage",
                                 urllib.parse.urlencode(reply)).read()
    return 'Message Recieved!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Nothing to see, please go away.', 404
