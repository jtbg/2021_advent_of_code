import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

with open(config['ASSETS']['input_file'], 'r') as f:
    readings = f.readlines()

readings = list(map(int, readings))

count_readings = 0
count_increased_depths = 0
for i in range(1, len(readings)):
    try:
        if readings[i] > readings[i-1]:
            count_increased_depths += 1
    except:
        print(f'''error at {count_readings+1} evaluating {readings[i]} > {readings[i-1]}''')
    finally:
        count_readings += 1

print(f'''Evaluated {count_readings} sonar readings and found {count_increased_depths} instances of increased depth''')
