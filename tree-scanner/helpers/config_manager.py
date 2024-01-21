import re


class ConfigManager:
    def __init__(self, path):
        self.file = open(path)
        self.text = self.file.read()

    def get_field(self, field_regex, parser):
        # Use a capture group in field
        # declarations e.g.
        # r'name = (\d+)'
        # This extracts the digit
        # part of the 'name' field.
        # This is then parsed
        matches = re.findall(f"\n{field_regex}\n", self.text)

        if len(matches) > 1:
            raise SyntaxError('Field assigned more than once')
        if len(matches) < 1:
            raise SyntaxError('Field not assigned')

        try:
            return parser(matches[0])
        except ValueError:
            raise ValueError('Field could not be parsed')
