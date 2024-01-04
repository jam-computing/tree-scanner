#!/usr/bin/env python

import asyncio
from websockets.server import serve
import re

path = 'localhost'
port = 8765

async def handle_request(websocket):
    for message in websocket:
        await websocket.send(message)

    def handle_message(message):
        if message.isdigit():
            wipe_update(int(message))
            websocket.send('Request processed')
        elif re.match(message, r'Setup Leds: \d+'):
            setup_ws281x()
        else:
            websocket.send('Bad request')

async def main():
    async with serve(handle_request, path, port):
        await asyncio.Future()  # run forever

asyncio.run(main())

def wipe_update(websocket, index):
    print(f'Received an led index : {index}')


def setup_ws281x()
