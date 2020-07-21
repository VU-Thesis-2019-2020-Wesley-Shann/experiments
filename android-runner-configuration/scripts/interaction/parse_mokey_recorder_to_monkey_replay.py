file_dir = '/home/sshann/Documents/thesis/experiments/android-runner-configuration/scripts/interaction/'
file_name_list = [
    'org.quantumbadger.redreader',
    'com.ak.uobtimetable',
    'appteam.nith.hillffair',
]

template_line_touch = '{"type": "touch", "x": %s, "y": %s, "down": %s, "up": %s, "sleep": %s }\n'
template_line_drag = '{"type": "drag", "points": [{"x": %s, "y": %s }, {"x": %s, "y": %s } ], "down": %s, "up": %s , "sleep": %s }\n'

for file in file_name_list:
    message = 'parsing file %s' % file
    border = ''.join([char * len(message) for char in '='])
    print(border)
    print(message)
    print(border)
    print('')
    src_file_path = file_dir + 'monkey_recorder/nexus_5x/' + file
    dst_file_path = file_dir + file
    dst_file = open(dst_file_path, 'w+')
    with open(src_file_path) as fp:
        line = fp.readline()
        down_count = 0
        up_count = 1
        cnt = 0
        while line:
            cnt += 1
            print("Line {}: {}".format(cnt, line.strip()))
            if line[0] == '#' or line == '\n':
                print('Ignore line')
                line = fp.readline()
                continue
            if '\'sleep\'' in line:
                sleep = line.split('\'sleep\':')[1].split(',')[0]
            else:
                sleep = '4'
            if '\'drag\'' in line:
                x1 = line.split('\'x1\':')[1].split(',')[0]
                y1 = line.split('\'y1\':')[1].split(',')[0]
                x2 = line.split('\'x2\':')[1].split(',')[0]
                y2 = line.split('\'y2\':')[1].split(',')[0]
                print('x1 = %s, y1 = %s, x2 = %s, y2 = %s, sleep = %s' % (x1, y1, x2, y2, sleep))
                parsed_line = template_line_drag % (x1, y1, x2, y2, down_count, up_count, sleep)
            else:
                x = line.split('\'x\':')[1].split(',')[0]
                y = line.split('\'y\':')[1].split(',')[0]
                print('x = %s, y = %s, sleep = %s' % (x, y, sleep))
                parsed_line = template_line_touch % (x, y, down_count, up_count, sleep)
            down_count += 2
            up_count += 2
            dst_file.write(parsed_line)
            line = fp.readline()
            print('')

    dst_file.close()
