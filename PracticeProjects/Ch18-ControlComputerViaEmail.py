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
a command.
'''

import logging
import imapclient
import USERNAMEANDPASSWORD as upw
import time
import pyzmail
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import pyinputplus as pyin

# Create logging file and input start of program call
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filename='programLog.txt')
logging.debug('start of program')

# Log into email
imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
imapObj.login(upw.email, upw.password)
imapObj.select_folder('INBOX', readonly=True)
print('Connection Established...')
logging.debug('Connection to email server established')

# Check for emails from specifc address every 15 minutes
# Check for password

def check_for_email():
    print('Searching...')
    UIDs = imapObj.search(
        ["FROM", upw.address_to_recieve_from, 'SUBJECT', 'download_file'])

    logging.debug('Searching for email in check_for_email()')

    if len(UIDs) >= 1:
        print('Email found...')
        logging.debug(f'Email found: {UIDs}')
        return(UIDs)
    else:
        # Wait 15 minutes
        time.sleep(900)


try:
    while True:
        UIDs = check_for_email()

        # Read contents of email
        logging.debug('Reading email')
        rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[0]][b'BODY[]'])

        # Find link in email
        utorrentLink = message.text_part.get_payload().decode(message.text_part.charset)
        logging.info(f'Link found: {utorrentLink}')

        # Idk what this line does
        tmp = os.popen("ps -Af").read()

        # Open uTorrent
        print('Opening torrent client...')
        logging.debug('Opening uTorrent if not already open')

        if 'uTorrent Web.app' not in tmp[:]:
            processuTorrent = subprocess.Popen(
                ['open', '/Applications/uTorrent Web.app'])

        # Send link to uTorrent
        browser = webdriver.Firefox()
        browser.get(
            'http://127.0.0.1:19575/gui/index.html?v=1.1.0.2856&localauth=localapi451c011519f98c09:#/library')

        time.sleep(1)
        addBtn = browser.find_element_by_id('auto-upload-btn')
        logging.debug('Upload Button')
        addBtn.click()

        time.sleep(1)
        textInput = browser.find_element_by_class_name('link-input')
        logging.debug('Entering text')
        textInput.send_keys(utorrentLink)

        time.sleep(1)
        addTorrentBtn = browser.find_element_by_id(
            'add-torrent-url-btn')
        logging.debug('Add Torrent accept button on first popup')
        addTorrentBtn.click()

        time.sleep(1)
        acceptCookie = browser.find_element_by_id('didomi-notice-agree-button')
        print('Accepting Cookies')
        acceptCookie.click()

        time.sleep(1)
        secondBtn = browser.find_element_by_class_name('add-torrent-btn')
        print('Add Torrent second button to start download')
        secondBtn.click()

        # Delete email
        print('Deleting email...')
        logging.debug(f'Delete email from {upw.email}')
        imapObj.select_folder('INBOX', readonly=False)
        imapObj.delete_messages(UIDs[0])
        imapObj.expunge()

        # Login to emails in preparatin for sending email
        logging.debug(f'Logging into {upw.email} with SMTP')
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(upw.email, upw.password)

        # Send email back confirming download started
        logging.debug('Email sent')
        smtpObj.sendmail(upw.email, upw.address_to_recieve_from,
                         'Subject: Your uTorrent Download.\n\nYour download has been started')

        # Killing conn to smtp
        smtpObj.quit()

except KeyboardInterrupt:
    print('Killing program...')
    imapObj.logout()

    killUTorrent = pyin.inputYesNo('Kill uTorrent? ')
    if response == 'yes':
        processuTorrent.terminate()
