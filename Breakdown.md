# Breakdown of the C++ Arduino code

```
#include <Wire.h> 
```
Imports a header file called Wire.h which allows the ToF to communicate with the nano over I2C (a protocol that has all the code which allows the proper communication between a low-power sensor and a microcontroller.)

``` 
#include <VL53L0X.h>
```
Pololu's version of the drivers (firmware) for this specific Tof sensor.

``` 
VL53L0X sensor;
```
Creates a VL53L0X object which we will call the methods of.

``` 
void setup() { }
```
All code inside the setup function runs at power-on.

``` 
Serial.begin(9600);
```
Opens a USB serial with a Baud rate of 9600. Baud is a unit of measurement that represents the number of distinct signals made per second in the specified channel.

``` 
Wire.begin();
```
Starts the I2C bus.

``` 
sensor.setTimeout(500);
```
Tells the sensor to give up trying and shutdown after 500ms of no signals.

``` 
if (!sensor.init()) { }
```
initializes the sensor and checks if it initialized correctly. If not, it prints "Sensor not found - check wiring" and hangs (freezes) which is useful for debugging.

> So the full if-block is:
> ```
>    if (!sensor.init()) {
>     Serial.println("Sensor not found - check wiring");
>     while (1) {}
>   }
> ```

``` 
sensor.startContinuous();
```
Puts the sensor in continuous measuring mode so that it is constantly measuring and sending data instead of only on request.

``` 
void loop() { }
```
The loop() function runs continuously forever.

``` 
uint16_t mm = sensor.readRangeContinuousMillimeters();
```
keeps sending the measurement as an unsigned 16 bit integer in millimeters.

``` 
  if (sensor.timeoutOccurred()) {
    Serial.println("Timeout");
  } else {
    Serial.print(mm);
    Serial.println(" mm");
  }
```
The if block checks if the sensor has timed out (no longer sending data) and if it is it will print "Timeout".
If not, it prints the number plus "mm".
