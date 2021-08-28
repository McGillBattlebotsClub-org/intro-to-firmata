import sys
import time

from pymata4 import pymata4
import keyboard  # using module keyboard
import serial
import time
from serial.tools import list_ports
import re #regex library

flagW = False
flagA = False
flagS = False
flagD = False
turnedOff = False
last = -1

up = ''
down = ''
left = ''
right = ''

# which control scheme to use for this robot
flag = False
while flag == False:
        g = input("Command scheme (0=wasd, 1 = tfgh): ")

        try:
            # ignore all occurences of key presses that could be caused by
            # controller presses.
            g = g.replace("w", "")
            g = g.replace("a", "")
            g = g.replace("s", "")
            g = g.replace("d", "")
            g = g.replace("t", "")
            g = g.replace("f", "")
            g = g.replace("g", "")
            g = g.replace("h", "")

            # convert parsed input to integer
            g = int(g)
            flag = True

            #insure that the user input is a valid index in the list
            if g < 0 or g > 1:
                flag = False
                print("Input out of bounds. Choose a scheme between 0 and 1")
        except:
            print("input must be a number")
            flag = False


if g == 0:
    up = 'w'
    down = 's' 
    left = 'a'
    right = 'd'
else:
    up = 't'
    down = 'g'
    left = 'f'
    right = 'h'


"""
Setup a pin for digital output and output a signal
and toggle the pin. Do this 4 times.
"""

# forward/backward motor
M1_1 = 4            # motor 1 pin 1
M1_2 = 5            # motor 1 pin 2
M1_PWM = 6          # motor 1 PWM pin

# L/R motor
M2_1 = 7            # motor 2 pin 1
M2_2 = 8            # motor 2 pin 2
M2_PWM = 9          # motor 2 PWM pin

def setup(my_board):
    global flagW, flagA, flagS, flagD, turnedOff, last, up, down, left, right
    
    my_board.keep_alive(period=5)
    
    # set the pin mode

    #FWD/BCK motor
    my_board.set_pin_mode_digital_output(M1_1)
    my_board.set_pin_mode_digital_output(M1_2)
    my_board.set_pin_mode_pwm_output(M1_PWM)

    #L/R motor
    my_board.set_pin_mode_digital_output(M2_1)
    my_board.set_pin_mode_digital_output(M2_2)
    my_board.set_pin_mode_pwm_output(M2_PWM)

    
    # get user controls and send to robot
    modulo = 3
    counter = 0
    counter = 0
    while True:
        if counter == 0:
            try:  # used try so that if user pressed other than the given key error will not be shown
                flagW = keyboard.is_pressed(up)
                flagA = keyboard.is_pressed(left)
                flagS = keyboard.is_pressed(down)
                flagD = keyboard.is_pressed(right)
                time.sleep(0.01)
            except:
                if last != 0:
                    turn_forward()
                    stop()
                    last = 0
        counter = (counter+1)% modulo
        dY = 0
        dX = 0
        if not (flagW and flagS):
            if flagW:
                dY = 1
            if flagS:
                dY = -1
        if not (flagA and flagD):
            if flagD:
                dX = 1
            if flagA:
                dX = -1

        if dY == 0 and dX == 0:
            if last != 0:
                print("idle")
                turn_forward()
                stop()
            last = 0
        elif dX == 0:
            if dY == 1:
                if last != 1:
                    print("up")
                    turn_forward()
                    forward()
                last = 1
            if dY == -1:
                if last != 2:
                    print("down")
                    turn_forward()
                    backward()
                last = 2
        elif dY == 0:
            if dX == 1:
                if last != 3:
                    print("right")
                    stop()
                    turn_right()
                    forward()
                last = 3
            if dX == -1:
                if last != 4:
                    stop()
                    print("left")
                    turn_left()
                    forward()
                last = 4
        
    my_board.shutdown()


def forward():
    board.digital_write(M1_1, 0)
    board.digital_write(M1_2, 1)
    board.pwm_write(M1_PWM, 255)

def backward():
    board.digital_write(M1_1, 1)
    board.digital_write(M1_2, 0)
    board.pwm_write(M1_PWM, 255)


def stop():
    board.pwm_write(M1_PWM, 0)
    board.digital_write(M1_1, 0)
    board.digital_write(M1_2, 0)

def turn_left():
    board.digital_write(M2_1, 0)
    board.digital_write(M2_2, 1)
    board.pwm_write(M2_PWM, 255)

def turn_right():
    board.digital_write(M2_1, 1)
    board.digital_write(M2_2, 0)
    board.pwm_write(M2_PWM, 255)


def turn_forward():
    board.pwm_write(M2_PWM, 0)
    board.digital_write(M2_1, 0)
    board.digital_write(M2_2, 0)
    
board = pymata4.Pymata4("COM6")
try:
    setup(board)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)

