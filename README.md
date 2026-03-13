# IoT Temperature Monitoring and Logging System

## Overview
This project monitors temperature using a DHT11 sensor and indicates different temperature levels using three LEDs. The system also displays temperature on a 16x2 LCD display and logs critical temperature events to Google Sheets.

## Features
- Temperature monitoring using DHT11
- LED indication for temperature levels
- Real-time temperature display on LCD
- Relay activation at critical temperature
- Data logging to Google Sheets

## Components
- ESP32 Microcontroller
- DHT11 Temperature Sensor
- 3 LEDs
- 220Ω Resistors
- 16x2 LCD Display
- 20k Potentiometer
- 2 Channel Relay Module
- Breadboard
- Jumper Wires

## Working
The sensor continuously reads the environmental temperature. Based on the value, LEDs indicate different levels. When the temperature crosses the critical threshold, the relay is activated and the timestamp is recorded in Google Sheets.

## Applications
- Smart home monitoring
- Industrial temperature monitoring
- Server room safety system
