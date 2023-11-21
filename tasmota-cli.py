import asyncio
import tasmotadevicecontroller
import argparse
import getpass
import json
import time

async def main(host, username, password, toggle):
    if username is None:
        device = await tasmotadevicecontroller.TasmotaDevice.connect(host)
    else:
        device = await tasmotadevicecontroller.TasmotaDevice.connect(url = host, username = username, password = password)

    if toggle:
        await device.setPower(tasmotadevicecontroller.tasmota_types.PowerType.TOGGLE)
        time.sleep(2)

    friendlyname = await device.getFriendlyName()
    power = await device.getPower()
    status8 = await device.sendRawRequest("status 8")
    watts = status8["StatusSNS"]["ENERGY"]
    print(json.dumps(watts, indent = 4))

    if power:
        print("'%s' is currently ON" % friendlyname)
    else:
        print("'%s' is currently OFF" % friendlyname)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--device-host",
    type = str,
    help = "Tasmota host port",
    required = True
)
parser.add_argument(
    "-u", "--user",
    type = str,
    help = "Username to login with"
)
parser.add_argument(
    "-t", "--toggle",
    action = "store_true",
    help = "Toggle current power status"
)

if __name__ == "__main__":
    args = vars(parser.parse_args())
    if args["user"] is not None:
        args["password"] = getpass.getpass("Input password for %s@%s: " % (args["user"], args["device_host"]))
    else:
        args["password"] = None
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args["device_host"], args["user"], args["password"], args["toggle"]))
