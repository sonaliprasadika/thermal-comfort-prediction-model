from machine import Pin, I2C
import network
import time
from bmp280 import BMP280
from umqtt.simple import MQTTClient
import ssl
import config

# Wi-Fi Configuration
ssid = config.ssid
password = config.pwd

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

connection_timeout = 50
while connection_timeout > 0:
    if wlan.status() == 3:  # Connected
        break
    connection_timeout -= 1
    print("[INFO] Waiting for Wi-Fi connection...")
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError("[ERROR] Failed to establish a network connection")
else:
    print("[INFO] CONNECTED!")
    print("[INFO] IP Address:", wlan.ifconfig()[0])

# Configure SSL Context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

# Connect to MQTT Broker
def connect_mqtt():
    try:
        client = MQTTClient(
            client_id=b'tumi_picow',
            server=config.MQTT_BROKER,
            port=config.MQTT_PORT,
            user=config.MQTT_USER,
            password=config.MQTT_PWD,
            ssl=context,
            keepalive=60 
        )
        client.connect()
        print("[INFO] MQTT connection successful")
        return client
    except Exception as e:
        print(f"[ERROR] MQTT connection failed: {e}")
        raise

client = connect_mqtt()

# Initialize BMP280 Sensor
i2c = I2C(id=1, sda=Pin(14), scl=Pin(15))
bmp = BMP280(i2c)

def publish(mqtt_client, topic, value):
    try:
        mqtt_client.publish(topic, value)
        print(f"[INFO][PUB] Published {value} to {topic}")
    except OSError as e:
        print(f"[ERROR] Failed to publish {value} to {topic}: {e}")
        reconnect(mqtt_client)

def reconnect(mqtt_client):
    try:
        mqtt_client.connect()
        print("[INFO] Reconnected to MQTT broker")
    except Exception as e:
        print(f"[ERROR] Reconnection failed: {e}")
        time.sleep(5)  # Retry after 5 seconds

# Main
while True:
    try:
        temp = bmp.temperature
        pressure = bmp.pressure
        publish(client, b'tumi_picow/temp', str(temp))
        publish(client, b'tumi_picow/pressure', str(pressure))
    except OSError as e:
        print(f"[ERROR] OSError occurred: {e}")
        reconnect(client)
    time.sleep(3)  
