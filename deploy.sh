#ampy  -p /dev/cu.usbmodem143101 put pico

device=/dev/cu.usbmodem141101

ampy  -p $device put detector/main.py
ampy  -p $device put detector/secret.py
ampy  -p $device put detector/wlan_util.py

ampy  -p $device mkdir lib
ampy  -p $device mkdir lib/umqtt
ampy  -p $device put lib/umqtt/simple.py lib/umqtt/simple.py


ampy  -p $device ls

#ampy  -p /dev/cu.usbmodem143101 reset

