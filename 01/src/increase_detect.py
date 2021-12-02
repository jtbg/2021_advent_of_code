import configparser

config = configparser.ConfigParser()
config.read('config.ini')

with open(config['ASSETS']['input_file'], 'r') as f:
    readings = f.readlines()

count_readings = 0
count_increased_depths = 0
for depth in readings:
    try:
        if depth > prev_depth:
            count_increased_depths += 1
    except NameError:
        print('no previous reading found')
    finally:
        prev_depth = depth
        count_readings += 1

print(f'''Evaluated {count_readings} sonar readings and found {count_increased_depths} instances of increased depth''')
