# The program will send good morning text messages to a particular number, everyday, every morning, between 6-7AM
# We need two Python Libraries,
# text-belts & schedule
# TEXTBELT ====> Handles sending of the messages
# SCHEDULE ======> HANDLES execution time.
# ========> from the website===> pypi.org/project/schedule/<==============
# =========> from the website======> textbelt.com<======

from Credentials import mobile_number
import requests
import schedule
import time


def send_message():
    resp = requests.post("https://textbelt.com/text", {
        "phone": mobile_number,
        "message": "Hey. Good morning",
        "key": "textbelt"
    })
    print(resp.json())


# schedule.every().day.at("06:00").do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
