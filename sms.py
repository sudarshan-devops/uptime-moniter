from twilio.rest import Client
tonum=""
smsbody=""

def SMS(tonum,smsbody):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                    body=smsbody,
                    from_='twillio number',
                    to=tonum
                    )

    print(message.sid)
