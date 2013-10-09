from flask import Flask
from db import SafetyDB
import json

app = Flask(__name__)
db = SafetyDB()

@app.route('/')
def hello_world():
    return 'I am up and running! Give me a url!'

@app.route('/<path:url>')
def checkurl(url):
    return json.dumps(db.checkUrl( url ))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    db.close()
