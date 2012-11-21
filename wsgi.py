import os, json

import requests as req
from flask import Flask, jsonify, request

from utils import get_customer_email, get_transaction_desc, msg_hipchat


CONF = json.loads(open('.env').read())
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify(response="Whatever...")


@app.route('/stripe/', methods=['POST'])
def stripe():
    def __buildLink(evt_id):
        return 'https://manage.stripe.com/#events/' + evt_id

    def __charge_succeeded(evt):
        charge = evt['data']['object']
        c = get_customer_email(charge['customer'])
        desc = get_transaction_desc(charge)
        amt = '$' + str(charge['amount'] / 100)
        return msg_hipchat('Not that I care, but ' \
                + c + ' just paid us ' + amt + ' for a ' + desc + \
                ' ' + __buildLink(evt['id']) + '.')

    def __charge_failed(evt):
        charge = evt['data']['object']
        c = get_customer_email(charge['customer'])
        desc = get_transaction_desc(charge)
        return msg_hipchat('Putting down my vinyl records to come tell you ' + \
                'compadres that ' + c + ' failed to pay us ' + \
                'for a ' + desc + '  ' + \
                __buildLink(evt['id']) + '.')


    notify = {
        'charge.succeeded':     __charge_succeeded,
        'charge.failed':        __charge_failed
    }

    evt = request.json
    resp = notify[evt['type']](evt)
    return jsonify(result='merp')



if __name__ == '__main__':
    port = int(CONF.get("PORT_WWW", 5000))
    app.run(debug=CONF.get("DEBUG", False), host='0.0.0.0', port=port)
