import json

import requests

CONF = json.loads(open('.env').read())

payload = '{"type":"charge.succeeded","pending_webhooks":1,"object":"event","created":1352517894,"livemode":true,"id":"evt_0hui0fwJ0RZYbJ","data":{"object":{"dispute":null,"refunded":false,"failure_message":null,"amount_refunded":0,"amount":9900,"fee_details":[{"type":"stripe_fee","currency":"usd","amount":317,"application":null,"description":"Stripe processing fees"}],"fee":317,"created":1352517893,"object":"charge","livemode":true,"paid":true,"invoice":null,"id":"ch_0huiypLI7UwOXA","currency":"usd","description":"Whitelabel - 08465b15997534c2f818c1a7b9b8b3:0","card":{"type":"Visa","exp_month":3,"address_zip":null,"exp_year":2015,"cvc_check":"unchecked","address_state":null,"address_zip_check":null,"object":"card","last4":"0849","address_country":null,"address_line1":null,"address_line1_check":null,"fingerprint":"nASiAJU2uVsN6Fpt","country":"US","name":null,"address_line2":null,"address_city":null},"customer":"cus_0hui7oMzSqfVse"}}}'
##payload = '{"type":"charge.failed","livemode":true,"object":"event","created":1351816908,"pending_webhooks":1,"id":"evt_0esHFitMMm43dQ","data":{"object":{"fee":0,"currency":"usd","paid":false,"customer":"cus_0YDTfZTxtjuXtk","fee_details":[{"amount":0,"type":"stripe_fee","description":"Stripe processing fees","currency":"usd","application":null}],"invoice":null,"livemode":true,"card":{"type":"Visa","exp_month":7,"address_line2":null,"address_zip_check":null,"exp_year":2014,"address_city":null,"address_line1_check":null,"object":"card","address_zip":null,"address_state":null,"last4":"1146","name":null,"address_country":null,"address_line1":null,"cvc_check":"unchecked","fingerprint":"dprXsyKHhDojgm8e","country":"US"},"failure_message":"Your card was declined.","created":1351816906,"object":"charge","refunded":false,"amount_refunded":0,"disputed":false,"amount":9900,"id":"ch_0esHLotnUNAIto","description":"Whitelabel - d925b9604d7edade1b221c0356e21d:2"}}}'

resp = requests.post('http://localhost:'+str(CONF['PORT_WWW'])+'/stripe/', 
                     data=payload,
                     headers={'content-type': 'application/json'})

print resp
