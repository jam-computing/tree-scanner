# import board


# For testing
class board(Enum):
    D10 = auto()
    D12 = auto()
    D18 = auto()
    D21 = auto()

def parse_pin(string):
    # Converts a string to a pin if it is valid
    # NeoPixels must be connected to D10, D12, D18 or D21 to work.
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

