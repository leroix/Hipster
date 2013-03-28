import os, json

import requests as req
from flask import Flask, jsonify, request

from utils import get_customer_email, get_transaction_desc, msg_hipchat


CONF = json.loads(open('.env').read()) if os.path.exists('.env') else os.environ
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify(response="Whatever...")


@app.route('/stripe/', methods=['POST'])
def stripe():
    def __build_send_msg(evt):
        charge = evt['data']['object']
        c = get_customer_email(charge['customer'])
        desc = get_transaction_desc(charge)
        return msg_hipchat(c + ' -- ' + desc + ' -- ' + '**' + evt['type'] + '**')

    evt = request.json
    if evt['type'] in ['charge.succeeded', 'charge.failed']:
        resp = __build_send_msg(evt)

    return jsonify(result='merp')



if __name__ == '__main__':
    port = int(CONF.get("PORT", 5000))
    app.run(debug=CONF.get("DEBUG", False), host='0.0.0.0', port=port)
