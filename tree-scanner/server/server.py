import asyncio
from websockets.server import serve
from ipaddress import ip_address

# import board
# import neopixel

from ...helpers.config_manager import ConfigManager
from led_manager import LedManager
from parsers import parse_pin

# Path to config file is within the ConfigManager constructor
config_manager = ConfigManager("../server.config")


def main():
    print("----- Scanner Server -----")
    print("Reading in data from the config...")

    # Variables from the config
    global ip, port, led_count, pin
    ip = config_manager.get_field(r"ip ?= ?(.+)", ip_address)
    port = config_manager.get_field(r"port ?= ?(\d+)", int)
    led_count = config_manager.get_field(r"led_count ?= ?(\d+)", int)
    pin = config_manager.get_field(r"pin ?= ?(.+)", parse_pin)

    print(f"IP: {ip}\nPort: {port}\nLed Count: {led_count}\nPin: {pin}")
    print("Accessing leds...")

    global led_manager
    led_manager = LedManager(pin, led_count)

    # Start the server
    print("Starting server...")
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
    print(f"Received message: {message}")

    if message.isdigit():
        index = int(message)
        print("Wipe update at index : " + index)
        led_manager.wipe_update(int(message))
        await websocket.send("request processed")
    elif message == "data":
        print("Data request")
        await websocket.send(
            f"IP: {ip} Port: {port} Led Count: {led_count} Pin: {pin}/"
        )
    elif message == "ping":
        print("Ping request")
        await websocket.send("pong")
    else:
        print("Bad request")
        await websocket.send("bad request")


if __name__ == "__main__":
    main()
