#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

int ledGreen = 16;
int ledYellow = 17;
int ledRed = 18;

void setup() {

Serial.begin(115200);

pinMode(ledGreen, OUTPUT);
pinMode(ledYellow, OUTPUT);
pinMode(ledRed, OUTPUT);

dht.begin();

}

void loop() {

float temp = dht.readTemperature();

Serial.print("Temperature: ");
Serial.println(temp);

if(temp < 30){

digitalWrite(ledGreen, HIGH);
digitalWrite(ledYellow, LOW);
digitalWrite(ledRed, LOW);

}

else if(temp >= 30 && temp < 40){

digitalWrite(ledGreen, LOW);
digitalWrite(ledYellow, HIGH);
digitalWrite(ledRed, LOW);

}

else{

digitalWrite(ledGreen, LOW);
digitalWrite(ledYellow, LOW);
digitalWrite(ledRed, HIGH);

}

delay(2000);

}
