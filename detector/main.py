from machine import Pin
import time
from wlan_util import WifiUtil

from umqtt.simple import MQTTClient

led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)


def send(counter):
    try:
        print("mqtt 1")
        c = MQTTClient("client_id", "10.100.0.104", port=1883, user=None, password=None, keepalive=30, ssl=False, ssl_params={})
        print("init mqtt")
        c.connect()
        print("Connected")
        c.publish(b"pump", str(counter))
        print("Published")
        c.disconnect()
        print("mqtt 2")
    except Exception as e:
        print("Failed to send mqtt")
        print(e)


def button_pressed(change):
    global button_pressed_count
    button_pressed_count += 1


print("start")
send(0)

# global value
button_pressed_count = 0
running_time = 0

wifi = WifiUtil()
wifi.init()

button.irq(handler=button_pressed, trigger=Pin.IRQ_FALLING)

active = False
ts = 0
button_pressed_count_old = 0
counter = 0
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
        running_time = running_time + (delta / 1000)

    time.sleep(0.5)

    if counter > 20:
        print(round(running_time))
        send(round(running_time))
        counter = 0
    counter = counter + 1

