import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

with open(config['ASSETS']['input_file'], 'r') as f:
    readings = f.readlines()

readings = list(map(int, readings))

count_readings = 0
count_increased_depths = 0

for i in range(3, len(readings) + 1):
    try:
        prev_window = sum(readings[i - 3 : i])
        this_window = sum(readings[i - 2 : i + 1])
        if this_window > prev_window:
            count_increased_depths += 1
    except:
        print('no previous reading found')
    finally:
        count_readings += 1

print(f'''Evaluated {count_readings} sonar readings and found {count_increased_depths} instances of increased depth''')