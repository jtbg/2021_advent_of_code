import logging


class SetSail:
    def __init__(self, vessel, course):
        self.my_vessel = vessel
        self.my_course = course
        logging.info(f'''setting sail on {self.my_vessel.name} from a position of {self.my_vessel.position}''')
        for movement in self.my_course.nav_steps:
            self.my_vessel.move(movement[0], movement[1])
        logging.debug(f'''sail completed after {self.my_vessel.odometer} steps. Final position: {self.my_vessel.position}''')


class Course:
    def __init__(self):
        self.nav_steps = []
        self.num_steps = 0

    def add_nav_step(self, direction=0, magnitude=0):
        self.num_steps += 1
        try:
            self.nav_steps.append([direction, int(magnitude)])
        except ValueError:
            print(f"Could not convert {magnitude} to an integer.")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def import_course(self, navfile_loc='./assets/course.txt'):
        with open(navfile_loc, 'r') as f:
            for line in f.readlines():
                direction, magnitude = line.strip().split(" ")
                self.add_nav_step(direction=direction, magnitude=magnitude)
        logging.debug("Navigation course parsed")
