import json

import requests

CONF = json.loads(open('.env').read())

payload = '{"type":"charge.succeeded","pending_webhooks":1,"object":"event","created":1352517894,"livemode":true,"id":"evt_0hui0fwJ0RZYbJ","data":{"object":{"dispute":null,"refunded":false,"failure_message":null,"amount_refunded":0,"amount":9900,"fee_details":[{"type":"stripe_fee","currency":"usd","amount":317,"application":null,"description":"Stripe processing fees"}],"fee":317,"created":1352517893,"object":"charge","livemode":true,"paid":true,"invoice":null,"id":"ch_0huiypLI7UwOXA","currency":"usd","description":"Whitelabel - 08465b15997534c2f818c1a7b9b8b3:0","card":{"type":"Visa","exp_month":3,"address_zip":null,"exp_year":2015,"cvc_check":"unchecked","address_state":null,"address_zip_check":null,"object":"card","last4":"0849","address_country":null,"address_line1":null,"address_line1_check":null,"fingerprint":"nASiAJU2uVsN6Fpt","country":"US","name":null,"address_line2":null,"address_city":null},"customer":"cus_0hui7oMzSqfVse"}}}'
#payload = '{"type":"charge.failed","livemode":true,"pending_webhooks":2,"object":"event","created":1353598940,"id":"evt_0mbKe0dFf0MxGY","data":{"object":{"dispute":null,"currency":"usd","refunded":false,"failure_message":"Your card was declined","fee_details":[{"type":"stripe_fee","amount":0,"currency":"usd","application":null,"description":"Stripe processing fees"}],"amount":799,"paid":false,"amount_refunded":0,"fee":0,"livemode":true,"created":1353598939,"object":"charge","card":{"last4":"5361","type":"Visa","exp_year":2018,"address_country":null,"address_zip_check":null,"address_line1":null,"fingerprint":"Hzg0nSVlbxkJbn4u","address_line1_check":null,"address_line2":null,"object":"card","address_city":null,"address_zip":null,"name":null,"exp_month":6,"country":"CA","address_state":null,"cvc_check":"unchecked"},"invoice":null,"customer":"cus_0mbJdDHs53xCvh","id":"ch_0mbJQnpq23uEzQ","description":null}}}'

resp = requests.post('http://localhost:'+str(CONF['PORT'])+'/stripe/', 
                     data=payload,
                     headers={'content-type': 'application/json'})

print resp
