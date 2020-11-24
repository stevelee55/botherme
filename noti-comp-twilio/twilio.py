# brew tap twilio/brew && brew install twilio

from twilio.rest import TwilioRestClient

export TWILIO_ACCOUNT_SID = 'ACe67392f33ee66107e86aa463abd08f39'
export TWILIO_AUTH_TOKEN = '4142d98493f025050b6e4ac9f25d1f3d'

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client.messages.create(from_='+18783132629',
                       to='__number__',
                       body='Ahoy from Twilio!')
