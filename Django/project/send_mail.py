import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from pathlib import Path
from django.conf import settings
import os

def send_invite(receiver_email: str, info: dict):
    context = ssl.create_default_context() # Create a secure SSL context
    sender_email = "mailbot.ace@gmail.com"

    try:
        with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/passwd.txt', 'rb') as f: # Need to manually create a txt file with your bot application password
            password = f.read().decode('utf-8')
    except Exception as e:
        print(1, str(e))
        return False

    message = MIMEMultipart()
    message["Subject"] = "ACE - 有新的協作邀請"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    try:
        with open(os.path.join(settings.BASE_DIR).replace('\\', '/') + '/project/static/mail_template.html', 'rb') as f:
            template = Template(f.read().decode('utf-8')) # Read a html file and replace some variable inside it 
        html = template.substitute(info)                  # with string.Template
        part = MIMEText(html, "html")
        message.attach(part)
    except Exception as e:
        print(2, str(e))
        return False

    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        try:
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, receiver_email, message.as_string())
        except Exception as e:
            print(3, str(e))
            return False
    
    return True
# print(send_invite(receiver_email='10846010@ntub.edu.tw', info={'activity_name': 'Trash', 'activity_description': 'Still trash', 'invitation_code': '123123'}))