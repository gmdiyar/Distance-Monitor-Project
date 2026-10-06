#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  sensor.setTimeout(500);
  if (!sensor.init()) {
    Serial.println("Sensor not found - check wiring");
    while (1) {}
  }
  sensor.startContinuous();
}

void loop() {
  uint16_t mm = sensor.readRangeContinuousMillimeters();
  if (sensor.timeoutOccurred()) {
    Serial.println("Timeout");
  } else {
    Serial.print(mm);
    Serial.println(" mm");
  }
}