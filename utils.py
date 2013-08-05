import os, json

import requests as req
import stripe

CONF = json.loads(open('.env').read()) if os.path.exists('.env') else os.environ
stripe.api_key = CONF['STRIPE_SECRET']

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

def get_customer_email(cid):
    return stripe.Customer.retrieve(cid)['email']

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


