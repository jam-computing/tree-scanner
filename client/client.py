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
    print('Welcome to the client of the scanner.\nEnsure the server is started. Please fill in the following options. Leaving them blank fills a default value')


    

def get_field(question, parser, default):
    while True:
        value = input()
        if value == '':
            return default
        try:
            return parser(value)
        except:
            print('Data invalid, try again')
   

if __name__ == '__main__':
    main()
