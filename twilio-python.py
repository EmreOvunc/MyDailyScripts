from twilio.rest import TwilioRestClient

account_sid = "YOUR SID" 
auth_token  = "YOUR AUTH" 

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Server is running...",
    to="YOURPHONENUMBER",    
    from_="YOURTWILIONUMBER") 

print(message.sid)
