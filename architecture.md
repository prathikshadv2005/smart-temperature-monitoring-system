# System Architecture

## Architecture Diagram

blob:https://web.whatsapp.com/075b093a-e49a-4cf7-8d8f-ed6509ae3bac

---

## Architecture Description

The IoT Based Temperature Monitoring System consists of a Raspberry Pi acting as the central processing unit. The DHT11 sensor collects temperature and humidity data from the surrounding environment and sends it to the Raspberry Pi.

The Raspberry Pi processes the sensor data and performs the following operations:

- Controls LED indicators to display the temperature status (normal, warning, or critical).
- Displays real-time temperature and humidity values on the 16x2 I2C LCD display.
- Activates the relay module to control external devices such as a fan or motor when the temperature crosses the defined threshold.

This architecture enables real-time monitoring and control of environmental temperature using IoT technology.
