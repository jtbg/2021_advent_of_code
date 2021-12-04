import journey
import logging
import vessel


def main():
    logging.basicConfig(level=logging.DEBUG)
    my_vessel = vessel.Submarine()
    my_vessel.diagnostics.bulk_input()
    logging.info(my_vessel.diagnostics.check_levels())



if __name__ == "__main__":
    main()
