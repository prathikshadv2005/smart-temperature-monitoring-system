# Circuit Connections

## DHT11 Temperature Sensor

| DHT11 Pin | ESP32 Connection |
|-----------|------------------|
| VCC | 3.3V |
| GND | GND |
| DATA | GPIO 4 |

---

## LED Connections

| LED | ESP32 Pin | Description |
|-----|-----------|-------------|
| Green LED | GPIO 16 | Low Temperature Indicator |
| Yellow LED | GPIO 17 | Medium Temperature Indicator |
| Red LED | GPIO 18 | High Temperature Indicator |

---

## Relay Module

| Relay Pin | ESP32 Connection | Purpose |
|-----------|------------------|---------|
| VCC | 5V | Power Supply |
| GND | GND | Ground |
| IN1 | GPIO 19 | Relay Control Signal |

---

## 16x2 LCD Display

| LCD Pin | ESP32 Connection |
|---------|------------------|
| RS | GPIO 21 |
| EN | GPIO 22 |
| D4 | GPIO 23 |
| D5 | GPIO 25 |
| D6 | GPIO 26 |
| D7 | GPIO 27 |
| VCC | 5V |
| GND | GND |
| V0 | Potentiometer (Contrast Control) |

---

## Potentiometer (20k)

| Potentiometer Pin | Connection |
|-------------------|-----------|
| Pin 1 | GND |
| Pin 2 (Middle) | LCD V0 |
| Pin 3 | 5V |
