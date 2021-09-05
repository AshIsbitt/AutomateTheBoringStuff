# Connecting to SMTP

import smtplib
import USERNAMEANDPASSWORD as upw

# Connect to this server on port 587
# If this doesn't work, use SMTP.SSL on port 465
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
print(smtpObj)

# smtpObj2 = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
# print(smtpObj2)

# Establish conn
print(smtpObj.ehlo())

# Start tls encryption
# Returning value 220 shows that the server is ready
print(smtpObj.starttls())

# Login to your email address
# Returning val 235 shows this was successful
print(smtpObj.login(upw.email, upw.password))

# Sending an email
# Args: sending email, recieving email, subject and content
# Third arg must start with "Subject \n" with a newline separating the subject from the body
# This will return a dict with each FAILED email sent.
smtpObj.sendmail(upw.email, upw.send_email,
                 'Subject: Testing.\n\nThis is an email sent through python')

# Disconnect
# Returning 221 means this was successful
print(smtpObj.quit())
