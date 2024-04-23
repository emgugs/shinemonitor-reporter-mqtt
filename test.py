import hashlib
import requests

# Authentication parameters
usr = 'hassan1khalid'  # Username
pwd = 'bigbang123'  # Password
company_key = 'bnrl_frRFjEz8Mkn'  # Company key
plant_id = '3053276'  # Plant ID
pn = 'Q0025061973396'  # Datalogger PN number
sn = 'Q002506197339609AD05'  # Device serial number
devcode = '2477'  # Device coding

# Function to calculate the sign using SHA-1 algorithm
def calculate_sign(salt, secret, token, action):
    data = f'{salt}{secret}{token}{action}'.encode('utf-8')
    sha1 = hashlib.sha1()
    sha1.update(data)
    sign = sha1.hexdigest()
    return sign

# Replace 'your_salt_value' and 'your_sign_value' with the actual values provided by ShineMonitor
salt = 'your_salt_value'
sign = 'your_sign_value'

# Set the headers with the token and sign
headers = {
    'Authorization': f'Bearer your_token_value',  # Replace 'your_token_value' with the actual token
    'Content-Type': 'application/json',
    'sign': sign
}

# Set the URL for fetching data
url = f'https://web.shinemonitor.com/public/?plant_id={plant_id}&pn={pn}&sn={sn}&devcode={devcode}'

# Make a GET request to fetch data
response = requests.get(url, headers=headers)

# Check the status code
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code} - {response.text}')