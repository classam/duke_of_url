from flask import Flask, Response, request
import json

from db import SafetyDB
import config

def url( hostname, port, path ):
    return hostname + ":" + str(port) + "/" + path

app = Flask(__name__)
db = SafetyDB()

@app.route('/')
def hello_world():
    return 'I am up and running! Give me a url!'

@app.route('/urlinfo/1/<hostname>:<int:port>/<path:path>', methods=['GET'])
def checkurl(hostname, port=80, path=""):
    return Response( 
            json.dumps(db.checkUrl( hostname + ":" + str(port) + "/" + path )),
            mimetype='application/json' )

@app.route('/urlinfo/1/<hostname>:<int:port>/<path:path>', methods=['PUT', 'POST'])
def createurl(hostname, port=80, path=""):
    if not 'status' in request.form or not 'reason' in request.form:
        return Response( "Invalid request. Please include a 'reason' and 'status' field") 
    status = request.form['status']
    reason = request.form['reason']
    if status not in ['SAFE', 'WARN', 'NOPE']:
        # Todo: proper error code. 
        return Response( "Invalid status. Please provide 'SAFE', 'WARN', or 'NOPE'")
    if not reason: 
        return Response( "You must provide a reason." )
    db.createUrl(url(hostname, port, path), hostname, port, path, status, reason )   
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
