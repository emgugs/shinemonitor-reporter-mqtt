debug = True  # True to enable, False to disable

# Shinemonitor settings
base_url = 'https://web.shinemonitor.com/public/'
usr = 'hassan1khalid'  # Username
pwd = 'bigbang123'  # Password
company_key = 'bnrl_frRFjEz8Mkn'  # Company key. Obtained from portal
plant_id = '3053276'  # Plant id (Power station ID). Obtained from portal.
pn = 'Q0025061973396'  # Datalogger PN number. Obtained from portal
sn = 'Q002506197339609AD05'  # Device serial number. Obtained from portal
devcode = '2477'  # Device coding. Obtained from portal

# MQTT settings
interval_in_minutes = 5
hostname = '38.7.189.156'
port = 1883
discovery_prefix = 'homeassistant'
base_topic = 'home/nodes'
sensor_name = 'shinemonitor-reporter'
mqtt_username = 'mqtt-user'  # MQTT broker username
mqtt_password = 'hassan123'  # MQTT broker password
