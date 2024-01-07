import asyncio
from websockets.server import serve
from ipaddress import ip_address

# import board
# import neopixel

from config_manager import ConfigManager
from led_manager import LedManager

# Path to config file is within the ConfigManager ctor
config_manager = ConfigManager("config")


def main():
    print("----- Scanner Server -----")
    print("Reading in data from the config")

    # Variables from the config
    ip = config_manager.get_field("ip ?= ?(.+)", ip_address)

    # Start the server
    asyncio.run(start_server())


async def start_server():
    async with serve(handle_request, path, port):
        await asyncio.Future()  # run forever


async def handle_request(websocket):
    for message in websocket:
        handle_message(websocket, message)


def handle_message(websocket, message):
    if message.isdigit():
        index = int(message)
        print("Wipe update at index : " + index)
        # wipe_update(int(message))
        websocket.send("Request processed")
    elif message == "setup":
        led_count = int(message[:11])
        print(f"Setting up {led_count} leds")
        # setup_ws281x(led_count)
        websocket.send("Setup complete")
    elif message == "data":
        print("Data request")
        # websocket.send(f"Path: {path}, Port: {port}, Leds: {led_count}")
    elif message == "ping":
        print("Ping request")
        websocket.send("pong")
    else:
        print("Bad request")
        websocket.send("Bad request")


if __name__ == "__main__":
    main()
