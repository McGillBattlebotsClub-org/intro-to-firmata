import serial
import time

s = serial.Serial(port='COM4',baudrate=115200,timeout=2)
time.sleep(1)
curTime = time.time_ns()
s.write(bytes('hello\r\n','utf-8'))
line = s.readline().decode("ISO8859")
print(line)
print("time = " + str((time.time_ns() - curTime)/1000000))
