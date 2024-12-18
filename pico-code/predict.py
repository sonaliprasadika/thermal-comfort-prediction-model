from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306
from bmp280 import BMP280
import model  # Import the model function

# Initialize the I2C bus and the OLED display
i2c = SoftI2C(scl=Pin(11), sda=Pin(10))

devices = i2c.scan()

if devices:
    print("I2C devices found:", [hex(dev) for dev in devices])
else:
    print("No I2C devices found")
    
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

dht22_sensor = dht.DHT22(Pin(22))

i2c_bmp = machine.I2C(id=1, sda=Pin(14), scl=Pin(15))
bmp_sensor = BMP280(i2c_bmp)

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
    if prediction == 1:
        green_led.on()  # Turn on green LED
        red_led.off()   # Turn off red LED
    elif prediction == 0:
        green_led.off() # Turn off green LED
        red_led.on()    # Turn on red LED
    else:
        green_led.off() # Turn off green LED
        red_led.off()   # Turn off red LED

while True:
    try:
        sleep(0.5)
        dht22_sensor.measure()
        
        # Read sensor values
        dht22_temp = dht22_sensor.temperature()
        dht22_hum = dht22_sensor.humidity()
        bmp_temp = bmp_sensor.temperature
        bmp_pressure = bmp_sensor.pressure / 100  # Convert to hPa
        mean_temp = (dht22_temp + bmp_temp) / 2

        # Prepare input for the model
        features = [mean_temp, dht22_hum, bmp_pressure]
#         print('%3.1f C, %3.1f %% , %3.1f hPa' % (mean_temp, dht22_hum, bmp_pressure))
        print('%3.1f,%3.1f,%3.1f' % (mean_temp, dht22_hum, bmp_pressure))

        # Predict using the model
        clf = model.RandomForestClassifier()
        prediction = clf.predict(features)

#         print(f"Prediction: {prediction}")
        
        update_display(dht22_temp, dht22_hum, bmp_pressure, prediction)
        update_led(prediction)
        
    except OSError as e:
        print("Failed to read sensor.")

