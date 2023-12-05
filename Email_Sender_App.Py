# Go over to our gmail account and setup 2 factor authentication
# Generate app password
# Create a function to send the mail
from email.message import EmailMessage
from App2 import password
import ssl
import smtplib


# lets add some variables
email_sender = "programmewithnambativep@gmail.com"
email_password = password

email_receiver = 'pbeng19@chupanhcuoidep.com'
subject = 'Dont forget to subscribe'
body = """
Please we encourage you to watch this video, then subscribe by hitting
the subscribe button
"""

# lets create an instance of the emailmessage
em = EmailMessage()
em['From'] = email_sender
em['To']   = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())






