import journey
import logging
import vessel


def main():
    logging.basicConfig(level=logging.INFO)
    my_vessel = vessel.Submarine()
    my_vessel.diagnostics.bulk_input()


if __name__ == "__main__":
    main()
