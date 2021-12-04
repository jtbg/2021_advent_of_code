import logging


class Sonar:
    def __init__(self):
        self.num_readings = 0
        self.readings = []

    def bulk_input(self, report_loc="./assets/sonar_readings"):
        with open(report_loc, 'r') as f:
            for line in f.readlines():
                self.add_reading(line)
        logging.debug(f'''bulk sonar file {report_loc} imported''')

    def add_reading(self, new_reading):
        self.num_readings += 1
        try:
            self.readings.append(int(new_reading))
        except ValueError:
            print(f"Could not convert {new_reading} to an integer.")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def count_increased_depths(self, sliding_window=1):
        cnt = 0
        sw = sliding_window - 1
        for i in range(0, len(self.readings) + 1):
            try:
                prev_window = self.readings[(i - sw - 1):i]
                this_window = self.readings[(i - sw):(i + 1)]
                if this_window > prev_window:
                    cnt += 1
            except IndexError as err:
                logging.debug(f'No previous reading found before position {i} with window size {sliding_window}')
            except BaseException as err:
                logging.error(f"Unexpected {err=}, {type(err)=}")
        return cnt
