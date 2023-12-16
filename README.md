# TasmotaCLI
Quick CLI script for turning on and off Tasmota-flashed plugs. Has scripts for both using the HTTP and MQTT APIs.

## Command line usage

```
usage: tasmota-http-cli.py [-h] -d DEVICE_HOST [-u USER] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE_HOST, --device-host DEVICE_HOST
                        Tasmota host port
  -u USER, --user USER  Username to login with
  -t, --toggle          Toggle current power status
```

```
usage: tasmota-mqtt-client.py [-h] [-m MQTT_HOST] -u USER [-t] -n FRIENDLYNAME

optional arguments:
  -h, --help            show this help message and exit
  -m MQTT_HOST, --mqtt-host MQTT_HOST
                        MQTT Server
  -u USER, --user USER  Username to login with
  -t, --toggle          Toggle current power status
  -n FRIENDLYNAME, --friendlyname FRIENDLYNAME
                        Device friendly name
```

## Example output

```
{
    "TotalStartTime": "2022-11-09T21:11:01",
    "Total": 144.706,
    "Yesterday": 0.361,
    "Today": 0.288,
    "Power": 16,
    "ApparentPower": 27,
    "ReactivePower": 22,
    "Factor": 0.58,
    "Voltage": 242,
    "Current": 0.113
}
'12VBrickPlug' is currently ON
```
