# tm1637

TM1637 seems to have I2C connectivity but it's not. Doesn't have slave address, and is LSB first like UART, not MSB first. 

Library to use multiple tm1637s on a Raspberry Pi

Connection

5v or 3.3V, and GND
- Display1:  CLK=13, DIO=12
- Display2:  CLK=19, DIO=16
- Display3:  CLK=26, DIO=20
- Display4:  CLK=21, DIO=22

```
python3 display.py
python3 worldclock.py
```
