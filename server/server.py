import asyncio
from websockets.server import serve
import board
import neopixel

# Connection variables
path = 'localhost'
port = 8765

# Led variables
board_pin = Board.D18
led_count = 50
led_manager = None

async def handle_request(websocket):
    for message in websocket:
        handle_message(websocket, message)

def handle_message(websocket, message):
    if message.isdigit():
        index = int(message)
        print('Wipe update at index : ' + index)
        wipe_update(int(message))
        websocket.send('Request processed')
    elif message == 'setup':
        led_count = int(message[:11])
        print(f'Setting up {led_count} leds')
        setup_ws281x(led_count)
        websocket.send('Setup complete')
    elif message == 'data':
        print('Data request')
        websocket.send(f'Path: {path}, Port: {port}, Leds: {led_count}')
    elif message == 'ping':
        print('Ping request')
        websocket.send('pong')
    else:
        print('Bad request')
        websocket.send('Bad request')

async def main():
    async with serve(handle_request, path, port):
        await asyncio.Future()  # run forever

def get_field(question, parser, default):
    print(question)
    while True:
        value = input()
        if value == '':
            return default
        try:
            return parser(value)
        except ValueError:
            print('Data invalid, try again')

def get_data():
    print('Before the server can start, please fill in the following data. Leaving the field blank will use a default')

    
   
def setup_ws281x():
    pass

if __name__ == '__main__':
    print('----- Scanner Server -----')


    asyncio.run(main())
