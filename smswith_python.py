# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACaa228100323eca550d656186c35f11b1'
auth_token = 'af83dcef94d626e71dde60f3716db902'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hi mom!!.",
                     from_='+12074776810',
                     to='+919871647833'
                 )

print(message.sid)
