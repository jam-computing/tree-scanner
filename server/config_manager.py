import re

class ConfigManager:
    def __init__(self, path):
        self.file = open(path)
        self.text = self.file.read()
        print(repr(self.text))

    def get_field(self, field_name, parser):
        # A field declaration is as follows
        # - The start of the line
        # - The field name
        # - 0 or 1 spaces
        # - An equals sign
        # - 0 or 1 spaces
        # - 1 or more charachters
        # - The end of the line
        matches = re.findall(r"\n" + field_name + r" ?= ?(.+)\n", self.text)

        if len(matches) > 1:
            raise SyntaxError('Field assigned more than once')
        if len(matches) < 1:
            raise SyntaxError('Field not assigned')

        try:
            return parser(matches[0])
        except ValueError:
            raise ValueError('Field could not be parsed')

