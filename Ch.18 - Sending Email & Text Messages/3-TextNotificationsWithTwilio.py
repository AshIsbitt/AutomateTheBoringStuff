# Sending texts via Twilio

from twilio.rest import Client
import USERNAMEANDPASSWORD as upd

accountSID = upd.twilio_account_sid
authToken = upd.twilio_token

twilioCli = Client(accountSID, authToken)
twilioNumber = '+14154631931'
message = twilioCli.messages.create(
    body="Howdy, Partner", from_=twilioNumber, to=upd.my_num)
