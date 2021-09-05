# Retrieving and deleting emails

import imapclient
import USERNAMEANDPASSWORD as upw
import pprint
import pyzmail

# Connect to server
imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)

# Log in to server
print(imapObj.login(upw.email, upw.password))

# Get list of folders
pprint.pprint(imapObj.list_folders())

# Select folder - set to readonly to prevent accidental deletions.
imapObj.select_folder('INBOX', readonly=True)

# Find UIDs of emails
UIDs = imapObj.search(["FROM", "service@paypal.co.uk", 'ON', '10-Jul-2021'])
print(UIDs)

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# pprint.pprint(rawMessages)

# Change folder to readonly=false to mark emails as read
imapObj.select_folder('INBOX', readonly=False)

# Get email address from raw message
# b before a string means it's a 'bytes' value, not a string value
message = pyzmail.PyzMessage.factory(rawMessages[8369][b'BODY[]'])

print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))

# Getting body of email
# This will be either html_part or text_part - you need the one that returns True
print(message.html_part != None)
print("*-" * 20)
# print(message.html_part.get_payload().decode(message.html_part.charset))

# Deleting email
#imapObj.delete_messages(UIDs[1])
print(imapObj.expunge())

# Disconnect
imapObj.logout()
