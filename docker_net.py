import docker
import os

def get_mqtt_addr():
    if os.getuid() != 0:
        raise Exception("You must be root to access the docker API and fetch the container's network")

    client = docker.from_env()
    containers = client.networks.get("poweredagay_default").attrs["Containers"]
    for k, v in containers.items():
        if "mqtt_1" in v["Name"]:
            return v["IPv4Address"].split("/")
