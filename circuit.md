# 🔌 Circuit Connections

## DHT11 Sensor Connection

| Component | Pin | Raspberry Pi Pin |
|-----------|-----|------------------|
| DHT11 | VCC | Pin 1 (3.3V) |
| DHT11 | GND | Pin 6 (GND) |
| DHT11 | DATA | Pin 7 (GPIO4) |

---

## LED Connections

| LED | Raspberry Pi Pin | GPIO |
|-----|------------------|------|
| Green LED | Pin 11 | GPIO17 |
| Yellow LED | Pin 13 | GPIO27 |
| Red LED | Pin 15 | GPIO22 |

⚠️ Each LED should be connected with a **220Ω resistor**.

---

## LCD Display (16x2 I2C) Connections

| LCD Pin | Raspberry Pi Pin |
|---------|------------------|
| GND | Pin 6 |
| VCC | Pin 4 (5V) |
| SDA | Pin 3 (GPIO2) |
| SCL | Pin 5 (GPIO3) |

---

## Relay Module Connection (Optional)

| Relay Pin | Raspberry Pi Pin |
|-----------|------------------|
| IN | Pin 16 (GPIO23) |
| VCC | Pin 2 (5V) |
| GND | Pin 6 (GND) |
