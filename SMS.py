from twilio.rest import Client
import GoogleMap as Gm
account_sid = 'AC10135a8333e2a0574fe98bddecc2a463'
auth_token = '889fa01d1bbe541cdd254ea991447a39'
client = Client(account_sid,auth_token)


def sendEmergencyText(text):
    client.messages.create(
        body=text,
        from_='+14302643436',
        to='+14379885306'
    )


def sendLocationOnPhone(location):
    client.messages.create(
        body="The Address Link is: " + Gm.search_location_in_city(location),
        from_='+14302643436',
        to='+14379885306'
    )
