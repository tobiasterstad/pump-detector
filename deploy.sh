#ampy  -p /dev/cu.usbmodem143101 put pico

ampy  -p /dev/cu.usbmodem144101 put detector/main.py
ampy  -p /dev/cu.usbmodem144101 put detector/secret.py
ampy  -p /dev/cu.usbmodem144101 put detector/wlan_util.py

ampy  -p /dev/cu.usbmodem144101 mkdir lib
ampy  -p /dev/cu.usbmodem144101 mkdir lib/umqtt
ampy  -p /dev/cu.usbmodem144101 put lib/umqtt/simple.py lib/umqtt/simple.py


ampy  -p /dev/cu.usbmodem144101 ls

#ampy  -p /dev/cu.usbmodem143101 reset

