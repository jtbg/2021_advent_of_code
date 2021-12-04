import logging

from coolname import generate


class Vessel:
    def __init__(self):
        self.name = 'The ' + ' '.join(x.capitalize() for x in generate(2))
        self.x_pos = 0
        self.y_pos = 0
        self.odometer = 0
        self.diagnostics = Diagnostics()


class Submarine(Vessel):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.aim = 0

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


class Diagnostics:
    def __init__(self):
        self.num_readings = 0
        self.bitwise_counts = {
            # each position for a reaching is represented by a count of the ones and zeros in that position:
            # position_in_reading: {
            #     0: count_of_zeros,
            #     1: count_of_ones
            # },
            0: {
                0: 0,
                1: 0,
            },
        }
        self.levels = {}

    def gamma_level(self):
        lvl_binary = ""
        for pos in self.bitwise_counts:
            lvl_binary = lvl_binary + str(max(pos, key=pos.get))
        self.levels["gamma"] = int(lvl_binary, 2)

    def epsilon_level(self):
        lvl_binary = ""
        for pos in self.bitwise_counts:
            lvl_binary = lvl_binary + str(min(pos, key=pos.get))
        self.levels["epsilon"] = int(lvl_binary, 2)

    def add_reading(self, new_reading):
        self.num_readings += 1
        for iteration, this_bit in enumerate(list(new_reading)):
            self.bitwise_counts.setdefault(iteration, {0: 0, 1: 0})[this_bit] += 1

    def bulk_input(self, report_loc="../assets/diagnostic_report.txt"):
        with open(report_loc, 'r') as f:
            for line in f.readlines():
                self.add_reading(line)
        logging.DEBUG(f'''bulk file {report_loc} imported''')
