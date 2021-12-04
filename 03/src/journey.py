import logging


class SetSail:
    def __init__(self, vessel, course):
        self.my_vessel = vessel
        self.my_course = course
        logging.info(f'''setting sail on {self.my_vessel.name} from horizontal offset {self.my_vessel.x_pos} and depth of {self.my_vessel.depth}''')
        for movement in self.my_course.navsteps:
            self.my_vessel.move(movement[0], movement[1])
        logging.info(f'''sail completed after {self.my_vessel.odometer} steps, with a final position pf {self.my_vessel.x_pos} and depth of {self.my_vessel.depth}''')


class Course:
    def __init__(self):
        self.navfile_loc = input("Location of the course plan [default '../assets/course.txt']: ") or "../assets/course.txt"
        self.navsteps = []
        with open(self.navfile_loc, 'r') as f:
            for line in f.readlines():
                direction, magintude = line.strip().split(" ")
                self.navsteps.append([direction, int(magintude)])
        logging.debug("Navigation course parsed")
