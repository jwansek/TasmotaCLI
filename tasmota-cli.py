import asyncio
import tasmotadevicecontroller
import argparse
import getpass

async def main(host, username, password):
    if username is None:
        device = await tasmotadevicecontroller.TasmotaDevice.connect(host)
    else:
        device = await tasmotadevicecontroller.TasmotaDevice.connect(url = host, username = username, password = password)

    friendlyname = await device.getFriendlyName()
    power = await device.getPower()
    status8 = await device.sendRawRequest("status 8")
    watts = status8["StatusSNS"]["ENERGY"]
    print(watts)

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


if __name__ == "__main__":
    args = vars(parser.parse_args())
    if args["user"] is not None:
        args["password"] = getpass.getpass("Input password for %s@%s: " % (args["user"], args["device_host"]))
    else:
        args["password"] = None
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args["device_host"], args["user"], args["password"]))
