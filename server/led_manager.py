# import board
# import neopixel
import re
from enum import auto, Enum

# For testing
class board(Enum):
    D10 = auto()
    D12 = auto()
    D18 = auto()
    D21 = auto()

class LedManager:
#    def __init__(self, board_pin, led_count):
#        self.pixels = neopixel.NeoPixel(board_pin,
#                                        led_count)
#    def wipe_update(self, index):
#        # Clear the pixels
#        self.pixels.fill((0, 0, 0))
#        # Set the led at the index to max luminosity
#        self.pixels[index] = (255, 255, 255)
#        # Display on pixels
#        self.pixels.show()

    @staticmethod
    def parse_pin(string):
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        pins = re.findall(r'D\d+', string)

        if len(pins) > 1:
            raise ValueError('The field was assigned multiple times')
        if len(pins) < 1:
            raise ValueError('The field was not assigned')

        match pins[0]:
            case 'D10':
                return board.D10
            case 'D12':
                return board.D12
            case 'D18':
                return board.D18
            case 'D21':
                return board.D21
            case _:
                raise ValueError('NeoPixels must be connected to D10, D12, D18 or D21 to work')

