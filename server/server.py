import asyncio
from websockets.server import serve
import re

path = 'localhost'
port = 8765

async def handle_request(websocket):
    for message in websocket:
        handle_message(websocket, message)

def handle_message(websocket, message):
    if message.isdigit():
        index = int(message)
        print('Wipe update at index : ' + index)
        wipe_update(int(message))
        websocket.send('Request processed')
    elif re.match(message, r'Setup Leds: \d+'):
        led_count = int(message[:11])
        print(f'Setting up {led_count} leds')
        setup_ws281x(led_count)
        websocket.send('Setup complete')
    elif message == 'ping':
        print('Ping request')
        websocket.send('pong')
    else:
        print('Bad request')
        websocket.send('Bad request')

async def main():
    async with serve(handle_request, path, port):
        await asyncio.Future()  # run forever

asyncio.run(main())

def wipe_update(websocket, index):
    pass

def setup_ws281x():
    pass

