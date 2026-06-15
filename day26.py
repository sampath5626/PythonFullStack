'''
import datetime
day = datetime.date.today()
print(day.ctime())


import calendar
import datetime

today = datetime.date.today()
year = 2022
month = 8
print(calendar.month(year,month))


import calendar
year = 2025
print(calendar.calendar(2026))
'''
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
sender_mail = "samram5626@gmail.com"
password = 'gkwpvzxxgwfjknoc'
reciver_mail = "charansaibera4@gmail.com"
target_time = '10:42'

sub = "Sending time for particular time"
message = "Dear Charan \n   Thank you for your interest in the Data Quality Analyst position at Randstad Enterprise in Hyderabad, Telangana, India. Unfortunately, we will not be moving forward with your application,but we appreciate your time and interest in Randstad Enterprise."

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        msg = EmailMessage()
        msg["sub"] = sub
        msg["From"] = sender_mail
        msg["To"] = reciver_mail
        msg.set_content(message)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender_mail, password)
                smtp.send_message(msg)

            print("Email sent successfully!")
            break  

        except Exception as e:
            print("Error:", e)
            break

    time.sleep(30)  
