import logging

from sailing import vessel, journey, instruments, diagnostics

current_day = 'day03'


class DailyRunners:
    def __init__(self):
        pass

    def day03(self):
        my_levels = diagnostics.Levels()
        my_levels.bulk_input()
        print(my_levels.check_levels())

    def day02(self):
        my_vessel = vessel.Submarine()
        my_course = journey.Course()
        my_course.import_course()
        my_journey = journey.SetSail(vessel=my_vessel, course=my_course)
        x,d = my_vessel.position['x'], my_vessel.position['depth']
        print(f'''x: {x}\ndepth: {d}\nroduct: {x*d}''')

    def day01(self):
        my_sonar = instruments.Sonar()
        my_sonar.bulk_input()
        print(f'''Single-reading increases: {my_sonar.count_increased_depths(sliding_window=1)}''')
        print(f'''3-reading window increases: {my_sonar.count_increased_depths(sliding_window=3)}''')


    def run(self, do: str):
        if hasattr(self, do) and callable(func := getattr(self, do)):
            func()


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    DailyRunners().run(current_day)
