#Use twilio API and register your self on twilio, paste autj_token and account_sid
#This app will make call at specific time and repeat it for 5 times after every 5mins
#Add audio to assets of twilio and paste the link in response tag

from datetime import datetime
from twilio.rest import Client
import time

t = "00:12:12"

account_sid = '##'
auth_token = '##'

client = Client(account_sid, auth_token)


#print(call.sid)


while True:

    #time.sleep(1)

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(current_time)

    if current_time == t:

        for i in range(5):
            call = client.calls.create(twiml = '<Response><Play loop="10">link of mp3</Play></Response>',
                               to = '##',
                               from_ = '##')
            print(call.sid)
            time.sleep(300)

        break

        
        
