import RPi.GPIO as GPIO
import board
import adafruit_dht
import requests
from time import sleep

# -----------------------------
# GPIO Setup
# -----------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED Pins (Physical Pins)
green_led = 11
yellow_led = 13
red_led = 15

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

# -----------------------------
# DHT11 Sensor Setup
# DATA Pin -> Physical Pin 7 (GPIO4)
# -----------------------------
dht_device = adafruit_dht.DHT11(board.D4)

# -----------------------------
# Temperature Thresholds
# -----------------------------
threshold_medium = 27
threshold_critical = 29

# -----------------------------
# Google Sheets Web App URL
# Replace with your URL
# -----------------------------
google_script_url = "PASTE_YOUR_GOOGLE_SCRIPT_URL_HERE"

print("Temperature Monitoring Started...")

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            print("Temperature:", temperature, "°C")
            print("Humidity:", humidity, "%")

            # LED Logic
            if temperature < threshold_medium:
                GPIO.output(green_led, True)
                GPIO.output(yellow_led, False)
                GPIO.output(red_led, False)
                status = "Normal"

            elif temperature < threshold_critical:
                GPIO.output(green_led, False)
                GPIO.output(yellow_led, True)
                GPIO.output(red_led, False)
                status = "Warning"

            else:
                GPIO.output(green_led, False)
                GPIO.output(yellow_led, False)
                GPIO.output(red_led, True)
                status = "Critical"

                # Send data to Google Sheets
                try:
                    requests.get(google_script_url,
                                 params={"temp": temperature, "hum": humidity})
                except:
                    print("Failed to send data to Google Sheets")

            print("Status:", status)
            print("---------------------------")

            sleep(3)

        except RuntimeError as error:
            print("Sensor error:", error.args[0])
            sleep(2)

except KeyboardInterrupt:
    print("Program Stopped")
    GPIO.cleanup()
