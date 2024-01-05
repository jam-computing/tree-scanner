import asyncio
from websockets.sync.client import connect
# import cv2 as cv

def main():
    get_data()

def get_data():
    print('----- Scanner Client -----')
    print('Welcome to the client of the scanner.\nEnsure the server is started.\nPlease fill in the following options. Leaving them blank fills in a default value')

    led_count = get_field('How many leds? ', int, 50)
    port = get_field('Which port? ', int, 8765)
    path = get_field('What is the path? ', str, '')
    
    print(f'Leds: {led_count}, Port: {port}, Path: {path}')

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
   
if __name__ == '__main__':
    main()
