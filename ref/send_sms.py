from twilio.rest import Client


account_sid = "AC588a9316ceab51e2f239260xyz"

auth_token = "2d9d1c7569dab610176a3e5xyz"

client = Client(account_sid,auth_token)

message_body = """ \n Sent from Vaccinater SMS client"""

client.messages.create(

    to =   "+917061579443",
    from_ = "+18189460463",
    body = message_body
 

)

