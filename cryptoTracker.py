import random
from bs4 import BeautifulSoup as soup
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import urllib3
import time as delay


### Crypto EMail Messaging ###

url = "https://robinhood.com/crypto/"  # add Crypto ticker

http = urllib3.PoolManager()

msg = MIMEMultipart('alternative')
sender = ''  # Add sender email
pswd = ''  # Add Password to sender email

wait_time = 0

while True:

    msg['Subject'] = 'Crypto {0} Update'.format('')  # add name of Crypto

    res = http.request("GET", url)
    data = soup(res.data, "html.parser")
    clock = datetime.datetime.now()
    crypto_price = '{0}'.format(data.find_all(
        class_="QzVHcLdwl2CEuEMpTUFaj")[0].text)

    if wait_time == 1:  # wait 5 minutes
        delay.sleep(500)
    if wait_time == 2:  # wait 10 minutes
        delay.sleep(600)
    if wait_time == 3:  # wait 30 minutes
        delay.sleep(1800)

    Crypto = crypto_price.strip('$').replace(',', '')
    print('{0} -> {1}'.format(datetime.datetime.now().strftime("%H:%M:%S"), float(Crypto)))
    if(float(Crypto) >= 0.07000 and float(Crypto) <= 0.07999):  # Input Crypto price Range
        msg['From'] = sender
        if wait_time == 1:
            msg['Subject'] = 'Crypto Update: [5-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 2:
            msg['Subject'] = 'Crypto Update: [10-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 3:
            msg['Subject'] = 'Crypto Update: [30-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
            wait_time = 0

        msg['To'] = ''  # receiver's email address
        port = 587
        x = "[add name of Crypto ] is between 0.070 and 0.079"
        msg_send = MIMEText('Time Check: {0}'.format(x), 'plain')
        msg.attach(msg_send)
        with smtplib.SMTP('smtp.gmail.com', port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(sender, pswd)
            mail.sendmail(sender, 'Receiver Email address', msg.as_string())
            if wait_time == 3:
                wait_time = 0
            else:
                wait_time += 1
    if(float(Crypto) >= 0.06000 and float(Crypto) <= 0.06999):  # Input Crypto price Range
        msg['From'] = sender
        if wait_time == 1:
            msg['Subject'] = 'Crypto Update: [5-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 2:
            msg['Subject'] = 'Crypto Update: [10-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 3:
            msg['Subject'] = 'Crypto Update: [30-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
            wait_time = 0

        msg['To'] = ''  # receiver's email address
        port = 587
        x = "[add name of Crypto ] is between 0.060 and 0.069"
        msg_send = MIMEText('Time Check: {0}'.format(x), 'plain')
        msg.attach(msg_send)
        with smtplib.SMTP('smtp.gmail.com', port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(sender, pswd)
            mail.sendmail(sender, 'Receiver Email address', msg.as_string())
            if wait_time == 3:
                wait_time = 0
            else:
                wait_time += 1

    if(float(Crypto) >= 0.05000 and float(Crypto) <= 0.05999):  # Input Crypto price Range
        msg['From'] = sender
        if wait_time == 1:
            msg['Subject'] = 'Crypto Update: [5-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 2:
            msg['Subject'] = 'Crypto Update: [10-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 3:
            msg['Subject'] = 'Crypto Update: [30-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
            wait_time = 0

        msg['To'] = ''  # receiver's email address
        port = 587
        x = "[add name of Crypto ] is between 0.050 and 0.059"
        msg_send = MIMEText('Time Check: {0}'.format(x), 'plain')
        msg.attach(msg_send)
        with smtplib.SMTP('smtp.gmail.com', port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(sender, pswd)
            mail.sendmail(sender, 'Receiver Email address', msg.as_string())
            if wait_time == 3:
                wait_time = 0
            else:
                wait_time += 1
    if(float(Crypto) >= 0.04000 and float(Crypto) <= 0.04999):  # Input Crypto price Range
        msg['From'] = sender
        if wait_time == 1:
            msg['Subject'] = 'Crypto Update: [5-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 2:
            msg['Subject'] = 'Crypto Update: [10-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
        if wait_time == 3:
            msg['Subject'] = 'Crypto Update: [30-Minute Mark Reminder] Price -> {0}'.format(
                Crypto)
            wait_time = 0

        msg['To'] = ''  # receiver's email address
        port = 587
        x = "[add name of Crypto ] is between 0.040 and 0.049"
        msg_send = MIMEText('Time Check: {0}'.format(x), 'plain')
        msg.attach(msg_send)
        with smtplib.SMTP('smtp.gmail.com', port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(sender, pswd)
            mail.sendmail(sender, 'Receiver Email address', msg.as_string())
            if wait_time == 3:
                wait_time = 0
            else:
                wait_time += 1

    delay.sleep(35)  # random.randint(35, 40))
