# Welcome to our Firmata coding repository
### Instead of creating custom Arduino scripts for each robot, we chose to use the Firmata protocol and have scripts run on a host computer instead

## reasoning
Communication between the PC and Arduino adds latency to the system, so why would we switch to a fully remote control system?
- We were already controlling the robot using a Python script- this was done in order to control the robot using a game controller. **Having a fully remote script does not add much latency when compared to our older framework, especially when we consider the fact that firmata allows for asynchronous detection of arduino response, instead of needing to poll**
- It allows us to have more complex behavior, since an arduino nano has limited processing power/ storage. **Offloading computations and logic onto the PC allows us to avoid those limitations.**

## Where is the proof?
- We wanted to give concrete proof of our latency claims, and made scripts in order to allow us-- and you-- to verify them. **You can find the scripts in the _latency_tests_ folder**

## Latency comparisons (in ms)
| Firmata (async response) | Regular Arduino Script & Python Script (polling) |
| ------- | -------------------------------------- |
| 32 ms   | 0.06 ms |

## Advantages of Firmata over custom Arduino+python scripts
- Arduino can be flashed with FirmataExpress script and embedded into the robot without having to worry about needing to reflash it with updated software
- Firmata simplifies the communication between the Arduino and host computer (1 line of code, and can use the firmata protocol instead of having to write your own)
- Communication time is constant, and doesn't rely on user writing code to wait-for/decode instructions
- Includes a keepalive function, which allows the arduino to detect when its connection to the host has been broken, and resets itself to ensure the robot does not behave dangerously when out of control