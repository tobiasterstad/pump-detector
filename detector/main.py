from machine import Pin
import time
from wlan_util import WifiUtil

from umqtt.simple import MQTTClient

import utime
import json

led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)


def blink(timeout=1.0):
    led = Pin("LED", Pin.OUT)
    led.value(1)
    utime.sleep(timeout)
    led.value(0)


def send(counter):
    try:
        c = MQTTClient("client_id", "10.100.0.10", port=1883, user=None, password=None, keepalive=30, ssl=False, ssl_params={})
        c.connect()
        data = {"id": "sewer_pump", "value": counter}
        c.publish(b"terstad/sewer", json.dumps(data))
        c.disconnect()
        print("Published")
    except Exception as e:
        print("Failed to send mqtt")
        blink(timeout=0.5)
        print(e)


def button_pressed(change):
    global button_pressed_count
    button_pressed_count += 1


def load_counter():
    c = 0
    try:
        with open("counter.txt", "r") as f:
            c = float(f.read())
            f.close()
    except:
        print("Failed to read counter from disk")
    return c


def save_counter(c):
    try:
        with open("counter.txt", "w") as f:
            f.write(str(c))
            f.close()
    except:
        print("Failed to read counter from disk")


print("start")
blink()

# global value
button_pressed_count = 0
counter = load_counter()

wifi = WifiUtil()
wifi.init()

blink()

button.irq(handler=button_pressed, trigger=Pin.IRQ_FALLING)

active = False
ts = 0
button_pressed_count_old = 0
i = 0
while True:
    if button_pressed_count_old != button_pressed_count:
        button_pressed_count_old = button_pressed_count
        if not active:
            print("turned on")
            active = True
            ts = time.ticks_ms()
    elif active:
        delta = time.ticks_diff(time.ticks_ms(), ts)
        print("Turned off: ", delta/1000)
        active = False
        counter = counter + (delta / 1000)
        save_counter(counter)

    time.sleep(0.5)

    if i > 20:
        print(round(counter))
        send(round(counter))
        i = 0
        blink(timeout=0.1)
    i = i + 1

