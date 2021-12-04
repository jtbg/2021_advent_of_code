import logging


class Levels:
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

    def add_reading(self, new_reading):
        self.num_readings += 1
        reading = list(new_reading.strip())
        for iteration, this_bit in enumerate(reading):
            self.bitwise_counts.setdefault(iteration, {0: 0, 1: 0})
            self.bitwise_counts[iteration][int(this_bit)] += 1

    def bulk_input(self, report_loc="./assets/diagnostic_report.txt"):
        with open(report_loc, 'r') as f:
            for line in f.readlines():
                self.add_reading(line)
        logging.debug(f'''bulk file {report_loc} imported''')

    def check_levels(self):
        self.gamma()
        self.epsilon()
        self.levels['power'] = self.levels['gamma'] * self.levels['epsilon']
        return self.levels

    def gamma(self):
        lvl_binary = ''
        for key, counts in self.bitwise_counts.items():
            lvl_binary += str(max(counts, key=counts.get))
        logging.debug(f'''gamma level calculated: {lvl_binary}''')
        self.levels["gamma"] = int(lvl_binary, 2)

    def epsilon(self):
        lvl_binary = ""
        for key, counts in self.bitwise_counts.items():
            lvl_binary += str(min(counts, key=counts.get))
        logging.debug(f'''epsilon level calculated: {lvl_binary}''')
        self.levels["epsilon"] = int(lvl_binary, 2)
