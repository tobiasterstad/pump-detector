from lib.umqtt.simple import MQTTClient


if __name__ == '__main__':

    print("mqtt 1")
    c = MQTTClient("umqtt_client", "10.100.0.104")
    c.connect()
    c.publish(b"pump", b"hej")
    c.disconnect()
    print("mqtt 2")