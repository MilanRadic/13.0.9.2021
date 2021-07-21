#import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail():
    print("start of function")
    message = Mail(
        from_email='remzo.hoti@gmail.com',
        to_emails='milankrka@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        print("using key")
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)


