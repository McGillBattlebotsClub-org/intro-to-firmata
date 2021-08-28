"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.
 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys
import time

from pymata4 import pymata4

"""
Setup a pin for digital output and output a signal
and toggle the pin. Do this until user stops script
"""

# some globals
DIGITAL_PIN = 13  # arduino LED pin number


def blink(my_board, pin):
    """
    This function will toggle a digital pin.
    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)

    # toggle the pin forever
    while True:
        print('ON')
        my_board.digital_write(pin, 1)
        time.sleep(1)
        print('OFF')
        my_board.digital_write(pin, 0)
        time.sleep(1)

    my_board.shutdown()


board = pymata4.Pymata4("COM6")
try:
    blink(board, DIGITAL_PIN)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
