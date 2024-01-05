import asyncio
from webeockets.sync.client import connect
import cv2 as cv

def main():
    pass

class data:
    def __init__(self, port, path, led_count):
        self.port = port
        self.path = path
        self.led_count = led_count

def get_data():
    print('----- Scanner Client -----')
    print('Welcome to the client of the scanner.\nEnsure the server is started.')
    led_count = -1
    while led_count <= 0:
        led_count = int(input('How many Leds? '))

    

if __name__ == '__main__':
    main()
