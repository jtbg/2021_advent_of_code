import logging
from coolname import generate


class Vessel:
    def __init__(self):
        self.name = 'The ' + ' '.join(x.capitalize() for x in generate(2))
        self.x_pos = 0
        self.depth = 0
        self.odometer = 0

    def move(self, direction, magnitude):
        magnitude = int(magnitude)
        self.odometer += 1
        if direction == "forward":
            self.x_pos += magnitude
        elif direction == "down":
            self.depth += magnitude
        elif direction == "up":
            self.depth -= magnitude
        else:
            logging.error(f'''invalid movement {direction} {magnitude}''')


class Course:
    def __init__(self, navfile_loc):
        self.navsteps = []
        with open(navfile_loc, 'r') as f:
            for line in f.readlines():
                direction, magintude = line.strip().split(" ")
                self.navsteps.append([direction, int(magintude)])
        logging.debug("Navigation course parsed")


class Journey:
    def __init__(self):
        self.navfile_loc = input("Location of the course plan [default '../assets/course.txt']: ") or "../assets/course.txt"
        self.my_vessel = Vessel()
        self.my_course = Course(self.navfile_loc)
        logging.debug(f'''new journey created''')

    def set_sail(self):
        logging.info(f'''setting sail on {self.my_vessel.name} from horizontal offset {self.my_vessel.x_pos} and depth of {self.my_vessel.depth}''')
        for movement in self.my_course.navsteps:
            self.my_vessel.move(movement[0], movement[1])
        logging.info(f'''navigation course executed with a final position of {self.my_vessel.x_pos} and depth of {self.my_vessel.depth}''')


def main():
    logging.basicConfig(level=logging.INFO)
    my_journey = Journey()
    my_journey.set_sail()
    logging.info(f''' position * depth = {my_journey.my_vessel.x_pos * my_journey.my_vessel.depth}''')


if __name__ == "__main__":
    main()
