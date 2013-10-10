from flask import Flask, Response
import json

from db import SafetyDB
import config


app = Flask(__name__)
db = SafetyDB()

@app.route('/')
def hello_world():
    return 'I am up and running! Give me a url!'

@app.route('/urlinfo/1/<hostname>:<int:port>/<path:path>')
def checkurl(hostname, port=80, path=""):
    return Response( 
            json.dumps(db.checkUrl( hostname + ":" + str(port) + "/" + path )),
            mimetype='application/json' )

@app.route('/urlinfo/1/<hostname>:<int:port>/')
def checkurl_nopath(hostname, port):
    return checkurl(hostname, port)

@app.route('/urlinfo/1/<hostname>/<path:path>')
def checkurl_noport(hostname, path):
    return checkurl(hostname, path=path)

@app.route('/urlinfo/1/<hostname>')
def checkurl_justhost(hostname):
    return checkurl(hostname)

if __name__ == '__main__':
    app.debug = True
    app.run(host=config.flask_host)
    db.close()
