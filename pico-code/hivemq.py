# Most of the following content is recieved from course materials
# provided by IoT course staff (exercise 3 folder in Moodle). 
# Content and changes made by our group are marked using comments. 
from machine import Pin, I2C
import network
import time
import json
from bmp280 import BMP280
import gc

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
    

import mip

mip.install("umqtt.robust")
mip.install("umqtt.simple")
from umqtt.simple import MQTTClient

# config ssl connection w Transport Layer Security encryption (no cert)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # TLS_CLIENT = connect as client not server/broker
context.verify_mode = ssl.CERT_NONE # CERT_NONE = not verify server/broker cert - CERT_REQUIRED: verify

# config ssl connection w Transport Layer Security encryption (cert required)
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_verify_locations('ccertificate.pem') # Load the certificate from path

# mqtt client connect
client = MQTTClient(client_id=b'tumi_picow', server=config.MQTT_BROKER, port=config.MQTT_PORT,
                    user=config.MQTT_USER, password=config.MQTT_PWD, ssl=context)

client.connect()


# define I2C connection and BMP
i2c = machine.I2C(id=1, sda=Pin(14), scl=Pin(15)) # id=channel
bmp = BMP280(i2c)


def publish(mqtt_client, topic, value):
    mqtt_client.publish(topic, value)
    print("[INFO][PUB] Published {} to {} topic".format(value, topic))


while True:
    # publish as MQTT payload
    #publish(client, 'picow/temp', str(bmp.temperature))
    #publish(client, 'picow/pressure', str(bmp.pressure))
    
    # ** code produced by group begins here, some parts are inspired by course material ** 

    # get timestamp to send with the sensor data. For evaluation purposes
    current_time = int(time.time() * 1000)
    # Subtract 2 hours (in milliseconds) because we are finland time 
    two_hours_in_ms = 2 * 60 * 60 * 1000  # 2 hours in milliseconds
    adjusted_time = current_time - two_hours_in_ms
    
    # *FOR BMP* send json payload with timestamp and sensor data 
    # temperature_payload = {
    #     "temperature": bmp.temperature,
    #     "timestamp": adjusted_time
    # }
    
    # pressure_payload = {
    #     "pressure": bmp.pressure,
    #     "timestamp": current_time
    # }
    

    # DHT22 PART STARTS HERE
    # NOTE import and initialize the DHT sensor stuff, it has not been done yet
    # also add the leds, ML etc

    # Read sensor values
    dht22_temp = dht22_sensor.temperature()
    dht22_hum = dht22_sensor.humidity()
    bmp_temp = bmp.temperature
    bmp_pressure = bmp.pressure / 100  # Convert to hPa
    mean_temp = (dht22_temp + bmp_temp) / 2
    
    # *FOR DHT* json payload with timestamp and sensor data
    temperature_payload = {
        "temperature": mean_temp,
        "timestamp": adjusted_time
    }
    
    pressure_payload = {
        "pressure": bmp_pressure,
        "timestamp": current_time
    }
    
    humidity_payload = {
        "humidity": dht22_hum,
        "timestamp": current_time
    }
    
    
    # publish data 
    publish(client, 'picow/temp', json.dumps(temperature_payload))
    publish(client, 'picow/pressure', json.dumps(pressure_payload))
    publish(client, 'picow/humidity', json.dumps(humidity_payload))

    
    # this part is for memory usage evaluation
    gc.collect()
    free_memory = gc.mem_free()
    allocated_memory = gc.mem_alloc()
    total_memory = free_memory + allocated_memory
    
    publish(client, 'picow/memory_free', str(free_memory))
    publish(client, 'picow/memory_allocated', str(allocated_memory))
    publish(client, 'picow/memory_total', str(total_memory))

    # every 2s
    time.sleep_ms(2000)
    