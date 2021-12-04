from coolname import generate
import logging


class Submarine:
    def __init__(self):
        self.name = 'The ' + ' '.join(x.capitalize() for x in generate(2))
        self.x_pos = 0
        self.depth = 0
        self.aim = 0
        self.odometer = 0

    def move(self, direction, magnitude):
        magnitude = int(magnitude)
        self.odometer += 1
        if direction == "forward":
            self.x_pos += magnitude
            self.depth += magnitude * self.aim
        elif direction == "down":
            self.aim += magnitude
        elif direction == "up":
            self.aim -= magnitude
        else:
            logging.error(f'''invalid movement {direction} {magnitude}''')
        logging.debug(f'''
        Moved {direction} {magnitude}.
            {self.__dict__}
        ''')


class Diagnostic:
    def __init__(self):
        pass
