from machine import Pin, I2C
import network
import time
from bmp280 import BMP280
from umqtt.simple import MQTTClient
import ssl
import config


# setup wifi
ssid = config.ssid
password = config.pwd

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() == 3: # connected
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    time.sleep(1)

# check if connection successful
if wlan.status() != 3: 
    raise RuntimeError('[ERROR] Failed to establish a network connection')
else: 
    print('[INFO] CONNECTED!')
    network_info = wlan.ifconfig()
    print('[INFO] IP address:', network_info[0])
    
# config ssl connection w Transport Layer Security encryption (no cert)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # TLS_CLIENT = connect as client not server/broker
context.verify_mode = ssl.CERT_NONE # CERT_NONE = not verifing server/broker cert / CERT_REQUIRED = verify

# mqtt client connect
client = MQTTClient(client_id=b'piyumi_picow', server=config.MQTT_BROKER, port=config.MQTT_PORT,
                    user=config.MQTT_USER, password=config.MQTT_PWD, ssl=context)

client.connect()

# define I2C connection and BMP
i2c = machine.I2C(id=1, sda=Pin(14), scl=Pin(15)) # id=channel
bmp = BMP280(i2c)
bmp_pressure = bmp.pressure / 100 # Converting Pa into hPa


def publish(mqtt_client, topic, value):
    mqtt_client.publish(topic, value)
    print("[INFO][PUB] Published {} to {} topic".format(value, topic))


while True:
    # publish as MQTT payload
    publish(client, 'node3_picow/temp', str(bmp.temperature))
    publish(client, 'node3_picow/pressure', str(bmp_pressure))

    # every 2s
    time.sleep_ms(2000)
