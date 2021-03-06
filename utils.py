import os, json, calendar, datetime

import requests as req
import stripe

CONF = json.loads(open('.env').read()) if os.path.exists('.env') else os.environ
stripe.api_key = CONF['STRIPE_SECRET']

def delta2month(ts):
    if ts == None:
        return ""

    table =     [ "first"
                , "second"
                , "third"
                , "fourth"
                , "fifth"
                , "sixth"
                , "seventh"
                , "eighth"
                , "ninth"
                , "tenth"
                , "twelfth"
                , "thirteenth"
                , "fourteenth"
                , "fifteenth"
                ]

    now = datetime.datetime.utcnow()

    ts_dt = datetime.datetime.fromtimestamp(ts)

    months = max(now.month - ts_dt.month + 12*(now.year - ts_dt.year), 0)

    if months < len(table):
        return table[months] + " month"
    else:
        return "month " + str(months+1)

def get_transaction_desc(charge):
    if charge['invoice']:
        inv = stripe.Invoice.retrieve(charge['invoice'])

        if inv['lines']['subscriptions']:
            plan = inv['lines']['subscriptions'][0]['plan']['name']
        else:
            plan = "[[no current subscription]]"

        return plan
    elif charge['description']:
        return charge['description']
    else:
        return ''

def get_customer_email_plan(cid):
    c = stripe.Customer.retrieve(cid)

    em = c['email']

    subs = c.get('subscription')
    plan = (subs and subs['plan']['name']) or 'freeloader'
    month = delta2month(subs.get('start'))

    return (em, plan, month)

def msg_hipchat(msg):
    params = {
        'format':     'json',
        'auth_token': CONF['HIPCHAT_TOKEN']
    }

    payload = {
        'room_id':    int(CONF['HIPCHAT_ROOM']),
        'from':       'Stripe',
        'message':    msg
    }

    headers = {'content-type': 'application/json'}

    return req.post(CONF['HIPCHAT_MSG_URL'], 
                    data=payload,
                    params=params,
                    headers={})


