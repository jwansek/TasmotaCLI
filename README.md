# TasmotaCLI
Quick CLI script for turning on and off Tasmota-flashed plugs

## Command line usage

```
usage: tasmota-cli.py [-h] -d DEVICE_HOST [-u USER] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE_HOST, --device-host DEVICE_HOST
                        Tasmota host port
  -u USER, --user USER  Username to login with
  -t, --toggle          Toggle current power status
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
