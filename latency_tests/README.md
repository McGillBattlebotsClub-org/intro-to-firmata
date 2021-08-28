# Latency test format for Firmata setup:
- The host computer will change the value of a digital pin, and logs the current time.
- This pin is connected to another digital pin, which is an input pin, through a resistor. Once the pin value changes, it will trigger a callback function.
- The host computer logs the time at which the callback function is called, and computes how long it took for the callback event to occur.

# Latency test format for Arduino script + Python controller
- The host computer will send an instruction to the Arduino 
- The arduino will decode the instruction and send back the instruction to the host computer
- The host computer waits for the arduino response and logs the time taken