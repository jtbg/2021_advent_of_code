import journey
import logging
import vessel


def main():
    logging.basicConfig(level=logging.INFO)
    my_vessel = vessel.Submarine()
    my_course = journey.Course()
    my_journey = journey.SetSail(my_vessel, my_course)
    logging.info(f''' position * depth = {my_journey.my_vessel.x_pos * my_journey.my_vessel.depth}''')


if __name__ == "__main__":
    main()
