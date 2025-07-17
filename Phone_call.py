import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env
load_dotenv()

# Get Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

# Initialize client
client = Client(account_sid, auth_token)

# Create the call
call = client.calls.create(
    to="+91XXXXXXXXXX",  # ✅ Your verified number (replace this)
    from_="+1XXXXXXXXXX",  # ✅ Your Twilio number
    url="http://twimlets.com/message?Message%5B0%5D=Hello%20Dhruv%2C%20this%20is%20a%20test%20call%20from%20your%20Python%20app."
)

# Print call SID and status
print(f"✅ Call initiated. Call SID: {call.sid}")
