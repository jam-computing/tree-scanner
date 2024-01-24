import asyncio
from websockets.sync.client import connect
import ipaddress
import tomllib


path = "../configs/client.toml"


async def main():
    print("----- Scanner Client -----")
    print("Ensure the server is started")
    print("Reading in data from the config...")

    read_in()

    print(f"Ip: {ip}\nPort: {port}")

    read_in()

    print("Attempting to connect to the server")

    websocket = start_connection()

    value = ""
    while value != "y":
        value = input("Would you like to start the scan? [Y/n] ")

    while True:
        websocket.send(input())
        print(websocket.recv())


def read_in():
    with open(path, "rb") as file:
        data = tomllib.load(file)

        global ip, port
        ip = ipaddress.ip_address(data["ip"])
        port = data["port"]


def start_connection():
    return connect(f"ws://{ip}:{port}")


if __name__ == "__main__":
    asyncio.run(main())
