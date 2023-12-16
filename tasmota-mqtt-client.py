import paho.mqtt.client as paho
import threading
import argparse
import getpass
import time
import json

SENT_EVENT = threading.Event()

class MQTTClient:

    switch_energy = None
    switch_power = None

    def __init__(self, host, friendlyname, username, password, message = None):
        self.host = host
        self.friendlyname = friendlyname
        self.username = username
        self.password = password
        self.message = message

        # print("Instantiated. Message:", message)

        self.mqtt_c = paho.Client("tasmota-cli", clean_session = True)

        self.mqtt_c.on_connect = self._on_connect_cb
        if message is None:
            self.mqtt_c.on_message = self._on_message_cb

        self.mqtt_c.username_pw_set(username = username, password = password)
        self.mqtt_c.connect(self.host, 1883, 60)
        self.mqtt_c.loop_forever()
    
    def _on_connect_cb(self, mqtt, userdata, flags, rc):
        # print("Connected to broker")
        if self.message is None:
            self.mqtt_c.subscribe("tele/%s/+" % self.friendlyname)

        else:
            self.mqtt_c.publish("cmnd/%s/Power" % self.friendlyname, payload = self.message)
            print("Sent message '%s' to topic 'cmnd/%s/Power'" % (self.message, self.friendlyname))
            SENT_EVENT.set()
            self.mqtt_c.disconnect()

    def _on_message_cb(self, mqtt, userdata, msg):
        # print('Topic: {0} | Message: {1}'.format(msg.topic, msg.payload))

        if msg.topic.split("/")[1] == self.friendlyname:
            if msg.topic.split("/")[2] == "SENSOR":
                self.switch_energy = json.loads(msg.payload.decode())["ENERGY"]
            elif msg.topic.split("/")[2] == "STATE":
                self.switch_power = json.loads(msg.payload.decode())["POWER"]
        
        if self.switch_power is not None and self.switch_energy is not None:
            self.mqtt_c.disconnect()



parser = argparse.ArgumentParser()
parser.add_argument(
    "-m", "--mqtt-host",
    type = str,
    help = "MQTT Server",
    default = "172.18.0.2",
)
parser.add_argument(
    "-u", "--user",
    type = str,
    help = "Username to login with",
    required = True
)
parser.add_argument(
    "-t", "--toggle",
    action = "store_true",
    help = "Toggle current power status"
)
parser.add_argument(
    "-n", "--friendlyname",
    help = "Device friendly name",
    type = str,
    required = True
)

if __name__ == "__main__":
    args = vars(parser.parse_args())
    if args["user"] is not None:
        args["password"] = getpass.getpass("Input password for %s@%s: " % (args["user"], args["mqtt_host"]))
    else:
        args["password"] = None

    if args["toggle"]:
        client = MQTTClient(args["mqtt_host"], args["friendlyname"], args["user"], args["password"], "TOGGLE")    
        # print("Waiting for event...")
        SENT_EVENT.wait()
        # print("Done waiting.")

    client = MQTTClient(args["mqtt_host"], args["friendlyname"], args["user"], args["password"])
    print(json.dumps(client.switch_energy, indent = 4))
    print("'%s' is currently %s" % (client.friendlyname, client.switch_power))
