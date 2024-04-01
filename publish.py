import json
import time
import paho.mqtt.client as mqtt

# Settings
interval_in_minutes = 5
hostname = '10.10.10.3'
port = 1883
discovery_prefix = 'homeassistant'
base_topic = 'home/nodes'
sensor_name = 'shinemonitor-reporter'
mqtt_username = 'mqtt-user'  # MQTT broker username
mqtt_password = 'hassan123'  # MQTT broker password

# MQTT broker settings
MQTT_BROKER = hostname
MQTT_PORT = port
MQTT_TOPIC = f"{base_topic}/{sensor_name}"

# Provided JSON data
json_data = """
{
  "err": 0,
  "desc": "ERR_NONE",
  "dat": [
    {"title": "id", "val": "7ca0220523a8deb346715727e790efeb"},
    {"title": "Timestamp", "val": "2024-03-31 21:45:04"},
    {"title": "Working State", "val": "Invert Mode"},
    {"title": "AC Input Voltage", "unit": "V", "val": "0.0"},
    {"title": "AC Input Frequency", "unit": "Hz", "val": "0.0"},
    {"title": "PV Input Voltage", "unit": "V", "val": "0.0"},
    {"title": "PV Input Power", "unit": "W", "val": "0"},
    {"title": "Battery Voltage", "unit": "V", "val": "49.1"},
    {"title": "Battery Capacity", "unit": "%", "val": "79"},
    {"title": "Battery Charging Current", "unit": "A", "val": "0"},
    {"title": "Battery Discharge Current", "unit": "A", "val": "6"},
    {"title": "Output Voltage", "unit": "V", "val": "229.9"},
    {"title": "Output Frequency", "unit": "Hz", "val": "50.0"},
    {"title": "Output Apparent Power", "unit": "VA", "val": "253"},
    {"title": "Output Active Power", "unit": "W", "val": "206"},
    {"title": "AC Output Load", "unit": "%", "val": "4"},
    {"title": "Machine Type", "val": "Energy Storage Inverter"},
    {"title": "Main CPU Version", "val": "2112"},
    {"title": "Secondary CPU Version", "val": "0"},
    {"title": "Battery Piece", "val": "48V(5KW)"},
    {"title": "Nonimal Output Apparent Power", "unit": "VA", "val": "6200"},
    {"title": "Nonimal Output Active Power", "unit": "W", "val": "6200"},
    {"title": "Nominal AC Voltage", "unit": "V", "val": "230"},
    {"title": "Nominal AC Current", "unit": "A", "val": "26"},
    {"title": "Rated Battery Voltage", "unit": "V", "val": "48.0"},
    {"title": "Nominal Output Voltage", "unit": "V", "val": "230"},
    {"title": "Nominal Output Frequency", "unit": "Hz", "val": "50.0"},
    {"title": "Nominal Output Current", "unit": "A", "val": "26"},
    {"title": "Record Fault Code", "val": "Enable"},
    {"title": "Battery Equalization", "val": "Prohibited"},
    {"title": "Battery Equalization Activated Immediately", "val": "Enable"},
    {"title": "Buzzer Alarm", "val": "Enable"},
    {"title": "Power Saving Mode", "val": "Prohibited"},
    {"title": "LCD Backlight", "val": "Prohibited"},
    {"title": "Overload Auto Restart", "val": "Prohibited"},
    {"title": "Over Temperature Auto Restart", "val": "Prohibited"},
    {"title": "Beeps While Primary Source Interupt", "val": "Prohibited"},
    {"title": "Auto Return To Default Display Screen", "val": "Prohibited"},
    {"title": "Transfer To Bypass @ Overload", "val": "Prohibited"},
    {"title": "Charger Source Priority", "val": "Solar only"},
    {"title": "Output Source Priority", "val": "Solar"},
    {"title": "AC Input Range", "val": "Appliance"},
    {"title": "Battery Type", "val": "Flooded"},
    {"title": "Output Frequency", "unit": "Hz", "val": "50"},
    {"title": "Max Total Charge Current", "unit": "A", "val": "30"},
    {"title": "Output Voltage", "unit": "V", "val": "230"},
    {"title": "Max Utility Charge Current", "unit": "A", "val": "40"},
    {"title": "Comeback Utility Mode Voltage Point Under (SBU Priority)", "unit": "V", "val": "46.0"},
    {"title": "Comeback Battery Mode Voltage Point Under (SBU Priority)", "unit": "V", "val": "54.0"},
    {"title": "Bulk Charging Voltage", "unit": "V", "val": "58.4"},
    {"title": "Floating Charging Voltage", "unit": "V", "val": "54.0"},
    {"title": "Low Battery Cut-off Voltage", "unit": "V", "val": "40.0"},
    {"title": "Battery Equalization Voltage", "unit": "V", "val": "58.4"},
    {"title": "Battery Equalized Time", "unit": "min", "val": "60"},
    {"title": "Battery Equalized Timeout", "unit": "min", "val": "120"},
    {"title": "Battery Equalization Interval", "unit": "day", "val": "30"},
    {"title": "Battery Status", "val": "Battery Discharge"},
    {"title": "PV Status", "val": "PV Undervoltage"},
    {"title": "Mains Status", "val": "Mains Abnormality"},
    {"title": "Load Status", "val": "Load On (Normal)"}
  ]
}
"""

# Parse JSON data
data = json.loads(json_data)

# Prepare message
message = json.dumps(data['dat'])

# Define on_connect event handler
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

# Define on_publish event handler
def on_publish(client, userdata, mid):
    print("Data published to MQTT broker")

# Connect to MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username
