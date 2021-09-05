# Project - Just text me

import USERNAMEANDPASSWORD as upd
from twilio.rest import Client

twilioNumber = '+14154631931'


def textMyself(message):
    twilioCli = Client(upd.twilio_account_sid, upd.twilio_token)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=upd.my_num)
