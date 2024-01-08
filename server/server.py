import asyncio
from websockets.server import serve
from ipaddress import ip_address

# import board
# import neopixel

from config_manager import ConfigManager
from led_manager import LedManager
from parsers import parse_pin

# Path to config file is within the ConfigManager ctor
config_manager = ConfigManager("config")


def main():
    print("----- Scanner Server -----")
    print("Reading in data from the config")

    # Variables from the config
    ip = config_manager.get_field("ip ?= ?(.+)", ip_address)
    port = config_manager.get_field('port ?= ?(\d+)', int)
    led_count = config_manager.get_field('led_count ?= ?(\d+)', int)
    pin = config_manager.get_field('pin ?= ?(.+)', parse_pin)

    print(f'IP: {ip}\nPort: {port}\nLed Count: {led_count}\nPin: {pin}')

    # Start the server
    print('Starting server')
    asyncio.run(start_server(str(ip), port))


async def start_server(path, port):
    # Start the server with the parameters on
    # the handle_request function
    async with serve(handle_request, path, port):
        await asyncio.Future()  # run forever


async def handle_request(websocket):
    async for message in websocket:
        await handle_message(websocket, message)


async def handle_message(websocket, message):

    print(f'Received message:\n{message}\n')

    if message.isdigit():
        index = int(message)
        print("Wipe update at index : " + index)
        # wipe_update(int(message))
        await websocket.send("Request processed")
    elif message == "setup":
        led_count = int(message[:11])
        print(f"Setting up {led_count} leds")
        # setup_ws281x(led_count)
        await websocket.send("Setup complete")
    elif message == "data":
        print("Data request")
        # websocket.send(f"Path: {path}, Port: {port}, Leds: {led_count}")
    elif message == "ping":
        print("Ping request")
        await websocket.send("pong")
    else:
        print("Bad request")
        await websocket.send("Bad request")


if __name__ == "__main__":
    main()

