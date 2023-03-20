from flask import Flask, render_template, request
from flask import _request_ctx_stack as stack
from json2html import json2html
import logging
import requests
import simplejson as json
import sys
# from functools import wraps

# Python wrapper to convert JSON into a human readable HTML Table representation.
# python 3.7以上会报cgi错误

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import http.client as http_client
# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1

httpbin = {
    "url": "https://httpbin.org/get"
}

app = Flask(__name__)


def trace():
    # @wraps(f)
    def decorator(f):
        def wrapper(*args, **kwargs):
            request = stack.top.request
            print(">>>>> Receive {0} {1}".format
                  (request.method, request.url))
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator


@app.route("/")
@app.route("/index.html")
@trace()
def hello():
    input = {
        "name": "tiptok02",
        "description": "Converts JSON to HTML tabular representation"
    }
    table = json2html.convert(
        json=input, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
    print(table)
    return render_template('index.html', serviceTable=table)


@app.route("/get")
@trace()
def get_httpbin():
    status, details = hello_httpbin()
    return json.dumps(details), status, {'Content-Type': 'application/json'}


def hello_httpbin():
    try:
        url = httpbin['url']
        res = requests.get(url, timeout=3.0)
    except BaseException:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, product details are currently unavailable for this book.'}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("usage: %s port" % (sys.argv[0]))
        sys.exit(-1)
    p = int(sys.argv[1])
    logging.info("start at port %s" % (p))

    if sys.platform == "linux":
        app.run(host=':', port=p, debug=True, threaded=True)
    else:
        app.run(host='0.0.0.0', port=p, debug=True, threaded=True)
