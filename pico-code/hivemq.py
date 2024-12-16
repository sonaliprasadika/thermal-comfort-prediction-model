from machine import Pin, I2C, SoftI2C
import network
import time
import json
from bmp280 import BMP280
from umqtt.simple import MQTTClient
import ssl
import config
import dht
import model
import ssd1306
import gc

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
context.verify_mode = ssl.CERT_NONE # CERT_NONE = not verify server/broker cert - CERT_REQUIRED: verify

# config ssl connection w Transport Layer Security encryption (cert required)
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_verify_locations('ccertificate.pem') # Load the certificate from path

# mqtt client connect
client = MQTTClient(client_id=b'tumi_picow', server=config.MQTT_BROKER, port=config.MQTT_PORT,
                    user=config.MQTT_USER, password=config.MQTT_PWD, ssl=context)

client.connect()

# Initialize the I2C bus and the OLED display
i2c = SoftI2C(scl=Pin(11), sda=Pin(10))

devices = i2c.scan()

if devices:
    print("I2C devices found:", [hex(dev) for dev in devices])
else:
    print("No I2C devices found")
    
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# define I2C connection and BMP
i2c = machine.I2C(id=1, sda=Pin(14), scl=Pin(15)) # id=channel
bmp = BMP280(i2c)
dht22_sensor = dht.DHT22(Pin(22))

green_led = Pin(16, Pin.OUT)
red_led = Pin(17, Pin.OUT)

# Function to update the OLED display
def update_display(temp, hum, pressure, predicted_value):
    oled.fill(0)  # Clear the display
    oled.text("Temp: {:.1f} C".format(temp), 0, 0)
    oled.text("Hum: {:.1f} %".format(hum), 0, 10)
    oled.text("Press: {:.1f} hPa".format(pressure), 0, 20)
    #oled.text("Pred: {}".format(predicted_value), 0, 30)
    oled.show()
    
# Function to update LED status based on prediction
def update_led(prediction):
    if prediction == 0:
        green_led.on()  # Turn on green LED
        red_led.off()   # Turn off red LED
    elif prediction == 1:
        green_led.off() # Turn off green LED
        red_led.on()    # Turn on red LED
    else:
        green_led.off() # Turn off green LED
        red_led.off()   # Turn off red LED
        
def publish(mqtt_client, topic, value):
    mqtt_client.publish(topic, value)
    print("[INFO][PUB] Published {} to {} topic".format(value, topic))


while True:
    # get timestamp to send with the sensor data. For evaluation purposes
    current_time = int(time.time() * 1000)
    # Subtract 2 hours (in milliseconds) because we are finland time 
    two_hours_in_ms = 2 * 60 * 60 * 1000  # 2 hours in milliseconds
    adjusted_time = current_time - two_hours_in_ms
    # publish as MQTT payload
    dht22_sensor.measure()
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
    
    # Prepare input for the model
    features = [mean_temp, dht22_hum, bmp_pressure]
    
    clf = model.RandomForestClassifier()
    prediction = clf.predict(features)
        
    publish(client, 'temp', str(mean_temp))
    publish(client, 'humidity', str(dht22_hum))
    publish(client, 'pressure', str(bmp_pressure))
    publish(client, 'prediction', str(prediction))
    
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

    update_display(dht22_temp, dht22_hum, bmp_pressure, prediction)
    update_led(prediction)
    # every 2s
    time.sleep_ms(2000)
