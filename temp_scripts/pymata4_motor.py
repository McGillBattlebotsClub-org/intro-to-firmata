import sys
import time

from pymata4 import pymata4

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
    """
    This function will to toggle a digital pin.
    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """
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

    
    # toggle the pin 4 times and exit
    while True:
        turn_left()
        time.sleep(1)
        turn_forward()
        time.sleep(1)
        turn_right()
        time.sleep(1)
        turn_forward()
        time.sleep(1)
        
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
