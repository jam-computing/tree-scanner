import asyncio
from websockets.sync.client import connect
import ipaddress
import tomllib
import scan_manager


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

    print("Getting server data")

    websocket.send("data")
    led_count = int(websocket.recv())
    print(f"The server has am led count of {str(led_count)}")

    value = ""
    while value != "y":
        value = input("Would you like to start the scan? [Y/n] ")

    scanner = scan_manager.Scanner()

    for i in range(led_count):
        # Tell the server to turn on the correct led
        websocket.send(str(i))
        message = websocket.recv()

        if message != "request processed":
            raise Exception("There was an error turing on the led")

        print(f"Taking photo of led {i}")
        scanner.scan_frame()


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
