import logging


class Levels:
    def __init__(self):
        self.binary_readings = []
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

    def refresh_bit_frequency(self, fresh_readings):
        fresh_bitwise_counts = {}
        for item in fresh_readings:
            self.update_bit_frequency(item, fresh_bitwise_counts)
        return fresh_bitwise_counts

    def update_bit_frequency(self, new_reading, bitwise):
        for iteration, this_bit in enumerate(list(new_reading)):
            bitwise.setdefault(iteration, {0: 0, 1: 0})
            bitwise[iteration][int(this_bit)] += 1

    def bulk_input(self, report_loc="./assets/diagnostic_report"):
        with open(report_loc, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                self.binary_readings.append(line)
                self.update_bit_frequency(line, self.bitwise_counts)
        logging.debug(f'''bulk file {report_loc} imported''')

    def check_levels(self):
        self.gamma()
        self.epsilon()
        self.oxygen()
        self.co2_scrubbers()
        self.levels['power'] = self.levels['gamma'] * self.levels['epsilon']
        self.levels['life_support'] = self.levels['oxygen'] * self.levels['co2_scrubbers']
        logging.info(self.levels)
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

    def bit_criteria_filter(self, filter_type="max"):
        filtered_readings = self.binary_readings
        filtered_bitwise = self.bitwise_counts
        for bit_pos in filtered_bitwise:
            readings = filtered_readings
            filtered_readings = []
            filtered_bitwise = self.refresh_bit_frequency(readings)
            count_zeros = filtered_bitwise[bit_pos][0]
            count_ones = filtered_bitwise[bit_pos][1]
            if filter_type == "max":
                freq_value = 0 if count_zeros > count_ones else 1
            elif filter_type == "min":
                freq_value = 1 if count_zeros > count_ones else 0
            logging.debug(f'''bit {bit_pos} is {freq_value}''')
            for reading_item in readings:
                if reading_item[bit_pos] == str(freq_value):
                    filtered_readings.append(reading_item)
                    # logging.debug(f'''keeping {reading_item}''')
            if len(filtered_readings) == 1:
                return filtered_readings[0]


    def oxygen(self):
        lvl_binary = self.bit_criteria_filter(filter_type="max")
        logging.debug(f'''o2 level calculated {lvl_binary}''')
        self.levels["oxygen"] = int(lvl_binary, 2)

    def co2_scrubbers(self):
        lvl_binary = self.bit_criteria_filter(filter_type="min")
        logging.debug(f'''scrubber level calculated {lvl_binary}''')
        self.levels["co2_scrubbers"] = int(lvl_binary, 2)

    def load_test_data(self):
        foo =[
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        for line in foo:
            self.binary_readings.append(line)
            self.update_bit_frequency(line, self.bitwise_counts)
