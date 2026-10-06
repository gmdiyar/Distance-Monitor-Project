# Distance-Monitor-Project

We used a VL53L0X time-of-fight sensor and an Arduino Nano to monitor distance in real time.

## Hardware

Take a look at the VL53L0X Pinout:

![diagram1](</assets/images/diagram1.png>)

1. Start connecting the Arduino Nano to the breadboard like so:

![diagram2](</assets/images/diagram3.png>)

2. Once the Nano is properly seated on the breadboard, give it power by connecting it the laptop via the USB (laptop) -> USB Type C (Nano).
3. Connect the VL53L0X to the breadboard like so:

![photo1](</assets/images/photo1.jpeg>)

4. Use the male-to-male jumper cables to connect the Nano to the VL53L0X. The connections between the two is as follows:

| Arduino Nano | VL53L0X |
| ------------ | ------- |
| 5V           | VIN     |
| GND          | GND     |
| A5           | SCL     |
| A4           | SDA     |

#### You should now be ready to continue to the software set-up.



## Software

### Downloading the Arduino IDE

1. Go to https://www.arduino.cc/en/software/
2. Download the IDE and go through the set-up process.

> **Make sure you allow the IDE to access to the USB bus. It will not recognize the Arduino Nano if you don't.**

### Downloading the VL53L0X Library by Pololu

1. Go to the library manager in the Arduino IDE.

![screenshot](screenshot1)

### Once the library is downloaded, you should be ready to upload the source code (Time-of-Flight-Source.ino) into the IDE.
