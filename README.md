### Agilent counter

# requirements
pyvisa (pip install pyvisa)

# how to use
The agilent 53131a counter can only communicate with the GPIB (so not the RS232) port. 
The python code writes on the serial connection. The commands are both some standard IEE 488.2 command (like 'IDN?') and SCPI commands. 
See chapter 2 in https://www.keysight.com/us/en/assets/9018-01066/programming-guides/9018-01066.pdf?success=true for further explanation.

