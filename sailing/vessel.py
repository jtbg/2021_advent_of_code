import logging

from coolname import generate


class Vessel:
    def __init__(self):
        self.name = 'The ' + ' '.join(x.capitalize() for x in generate(2))
        print(f'''Welcome aboard {self.name}!''')
        self.position = {'x': 0, 'y': 0, }
        self.odometer = 0


class Submarine(Vessel):
    def __init__(self):
        super().__init__()
        self.position['depth'] = 0
        self.position['aim'] = 0

    def move(self, direction, magnitude):
        magnitude = int(magnitude)
        self.odometer += 1
        if direction == "forward":
            self.position['x'] += magnitude
            self.position['depth'] += magnitude * self.position['aim']
        elif direction == "down":
            self.position['aim'] += magnitude
        elif direction == "up":
            self.position['aim'] -= magnitude
        else:
            logging.error(f'''invalid movement {direction} {magnitude}''')
            logging.debug(f'''
        Moved {direction} {magnitude}.
            {self.position.__dict__}
        ''')
