'''
SMPT- Simple Mail Transfer Protocol
-----------------------------------
--> This is used to send emails from server to severes to another...
NOte:
------
1.SMPT SSL Port
---------------
465

2. SMTP TLS Port
-----------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'
'''
'''
import smtplib
from email.message import EmailMessage
sender = 'samram5626@gmail.com'
password= 'fajmpvkyquahaxws'
sam = EmailMessage()


sam['Subject']='Welcome Mail'
sam['From']=sender
sam['To']='harshaguttula07@gmail.com'

sam.set_content('Hii May JESUS save you today')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(sam)
server.quit()
'''
import smtplib
from email.message import EmailMessage

sender = 'samram5626@gmail.com'
password = 'jphxiwqwsqpugngm'
reciver = ['harshaguttula07@gmail.com','charansaibera4@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)

for email in reciver:
    sam = EmailMessage()
    sam['Subject']= 'Welcome Mail'
    sam['From']=sender
    sam['To']= email
    sam.set_content('HAI their is exam in next few minitus')
    server.send_message(sam)
ser1ver.quit()

















































