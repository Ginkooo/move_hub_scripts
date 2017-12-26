#!/bin/env python2

import pylgbst
from time import sleep
from pynput import keyboard
from functools import partial

from pylgbst import BLEConnection, MoveHub

connection = BLEConnection().connect(hub_mac='00:16:53:AA:B6:AC')

hub = MoveHub(connection)
print('Wait 10 s...')
sleep(10)
print('Ready!')

def on_press(key):
    if key == keyboard.Key.esc:
        print('ESC!\tAborting...')
        raise StopIteration()
    moves = {
            'w': partial(hub.motor_AB.timed, 0.4),
            'a': partial(hub.motor_B.timed, 0.4),
            'd': partial(hub.motor_A.timed, 0.4),
            's': partial(hub.motor_AB.timed, 0.4, -1),
            }
    try:
        moves[key.char]()
    except:
        print('Bad key')

def on_release(key):
    pass

try:
    with keyboard.Listener (
            on_press=on_press,
            on_release=on_release
            ) as listener:
        listener.join()
except StopIteration:
    pass
