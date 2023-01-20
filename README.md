# Agilent counter
The sole purpose of this program is to communicate with the device via python. It is a work in progress, other features (like setting trigger level) will be updated when necesarry ;).

Tested on windows machine with python 3.10.

## requirements
pyvisa (pip install pyvisa)

## how to use
The agilent 53131a counter can only communicate with the GPIB (so not the RS232) port. 
The python code writes on the serial connection. The commands are both some standard IEE 488.2 command (like 'IDN?') and SCPI commands. 
See chapter 2 in https://www.keysight.com/us/en/assets/9018-01066/programming-guides/9018-01066.pdf?success=true for further explanation.

## some tips
When using a GPIB to usb cable, make sure that the GPIB make a real electrical connection. I needed to screw of the cover of the male GPIB part to make sure it fitted.

Make sure you can find the device (using NI MAX). Only worked for me if the GPIB adres on the counter was set to 3 (standard factory setting), check by holding RECALL pressed and turning off and on your counter, scroll through menu using the RECALL button.


