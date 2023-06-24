#!C:\Python39\python.exe

import smtplib
import ssl
from email.message import EmailMessage
import cgi
# from decouple import config 
# solve why decouple import is not working

# form inputs
form_inputs = cgi.FieldStorage()
form_inputs.getvalue('site-url')
email_receiver = form_inputs.getvalue('email')
form_inputs.getvalue('interval')

# email sender credentials
email_sender = 'yumulacdev@gmail.com'
email_password = 'ottbyukuroqjhbqx'

# email message
subject = 'Your Job Ad Scraping Results are Ready!'
body = """
test email body, will be job ad scraping results
"""

# email message instance
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# security
context = ssl.create_default_context()

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())