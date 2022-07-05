from flask import Flask, request, redirect, url_for
import json
import sys
sys.path.insert(0, '../')

from Services import tweetsService as ts
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route('/trend-topics', methods = ['GET'])
def getTrendTopics():
    return json.dumps(ts.obtemTrendTopics(), indent=6)

@app.route('/trend-topics-e-links', methods = ['GET'])
def getTrendTopicsELink():
    return json.dumps(ts.obtemTrendTopicsELinks(), indent=6)


@app.route('/get', methods = ['GET'])
def get_hello_testing():
    return json.dumps(ts.getProfileTweets(request.args['query']), indent=6)


if __name__ == "__main__":
    app.run(debug=True)
