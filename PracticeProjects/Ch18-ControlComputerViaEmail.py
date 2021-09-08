# Chapter 18 - Control computer via emails

'''
Write a program that checks an email account every 15 minutes for any instructions you email it and
executes those instructions automatically.

For example, BitTorrent is a peer-to-peer downloading system. Using free BitTorrent software such as
qBittorrent, you can download large media files on your home computer. If you email the program a
(completely legal, not at all piratical) BitTorrent link, the program will eventually check its email, find
this message, extract the link, and then launch qBittorrent to start downloading the file. This way, you
can have your home computer begin downloads while you’re away, and the (completely legal, not at all
piratical) download can be finished by the time you return home.

Of course, you’ll want the program to make sure the emails come from you. In particular, you might want to
require that the emails contain a pass- word, since it is fairly trivial for hackers to fake a “from”
address in emails. The program should delete the emails it finds so that it doesn’t repeat instructions
have the program email or text you a confirmation every time it executes a command. Since you won’t be
sitting in front of the computer that is running the program, it’s a good idea to use the logging
functions to write a text file log that you can check if errors come up every time it checks the email
account. As an extra feature, have the program email or text you a confirmation every time it executes
a command. Since you won’t be sitting in front of the computer that is running the program, it’s a good
idea to use the logging functions (see Chapter 11) to write a text file log that you can check if errors
come up.
'''

import imapclient
import USERNAMEANDPASSWORD as upw
import time
import pyzmail
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

# Log into email
imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
imapObj.login(upw.email, upw.password)
imapObj.select_folder('INBOX', readonly=True)
print('Connection Established...')

# Check for emails from specifc address every 15 minutes
# Check for password


def check_for_email():
    print('Searching...')
    UIDs = imapObj.search(
        ["FROM", upw.address_to_recieve_from, 'SUBJECT', 'download_file'])

    if len(UIDs) >= 1:
        print('Email found...')
        return(UIDs)
    else:
        # Wait 15 minutes
        time.sleep(900)


try:
    while True:
        UIDs = check_for_email()

        # Read contents of email
        rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[0]][b'BODY[]'])

        # Find link in email
        utorrentLink = message.text_part.get_payload().decode(message.text_part.charset)

        # Idk what this line does
        tmp = os.popen("ps -Af").read()

        # Open uTorrent
        print('Opening torrent client...')
        if 'uTorrent Web.app' not in tmp[:]:
            subprocess.Popen(['open', '/Applications/uTorrent Web.app'])

        # Send link to uTorrent
        browser = webdriver.Safari()
        browser.get(
            'http://127.0.0.1:19575/gui/index.html?v=1.1.0.2856&localauth=localapi451c011519f98c09:#/library')

        time.sleep(1)
        addBtn = browser.find_element_by_id('auto-upload-btn')
        addBtn.click()

        time.sleep(1)
        textInput = browser.find_element_by_class_name('link-input')
        textInput.send_keys(utorrentLink)

        time.sleep(2)
        secondBtn = browser.find_element_by_class_name('add-torrent-btn')
        secondBtn.click()

        # Delete email
        print('Deleting email...')
        imapObj.select_folder('INBOX', readonly=False)
        imapObj.delete_messages(UIDs[0])
        imapObj.expunge()

        # Login to emails in preparatin for sending email
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(upw.email, upw.password)

        # Send email back confirming download started
        smtpObj.sendmail(upw.email, upw.address_to_recieve_from,
                         'Subject: Your uTorrent Download.\n\nYour download has been started')

        # Killing conn to smtp
        smtpObj.quit()

except KeyboardInterrupt:
    print('Killing program...')
    imapObj.logout()
