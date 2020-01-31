'''
THINGS WE CARE ABOUT FROM THESE DATASETS

HEADERS
1. ID (first field, index 0)
- To be printed during file processing
2. Name (second field, index 1)
- To be printed during file processing

ROWS
1. date (first field, index 0)
- To find date range of storm, print during file processing
- To associate storm with appropriate year, for output file
2. Record identifier (third field, index 2)
- To calculate number of landfalls, print during file processing
3. Maximum sustained wind (sixth field, index 5)
- To find highest sustained wind speed during storm lifetime, print during file processing
- To determine storm category, for output file
4. Minimum pressure (seventh field, index 6)
- To calculate change in pressure, print during file processing
'''


def hurc_handler(infile, last_pos):
    hurc_dict = dict()

    internal_last_pos = last_pos
    infile.seek(last_pos)

    header = infile.readline()
    header_split = header.split()
    hurc_dict['id_num'] = header_split[0][:-1]
    hurc_dict['name'] = header_split[1][:-1]

    line = infile.readline()
    # https://stackoverflow.com/questions/29618936/how-to-solve-oserror-telling-position-disabled-by-next-call
    while line:
        line_fields = line.split()

        if line_fields[0][0].isnumeric():
            internal_last_pos = infile.tell()

            hurc_date_list = [int(line_fields[0][0:4]), int(line_fields[0][4:6]), int(line_fields[0][6:8])]
            hurc_dict["end_date"] = hurc_date_list
            if not hurc_dict.setdefault("start_date"):
                hurc_dict["start_date"] = hurc_date_list

            hurc_code = line_fields[2][:-1]
            hurc_landfalls = hurc_dict.setdefault('landfall_count', 0)
            if hurc_code == 'L' and hurc_landfalls:
                hurc_dict['landfall_count'] += 1
            elif hurc_code == 'L':
                hurc_dict['landfall_count'] = 1

            hurc_wspeed = float(line_fields[6][:-1])
            if hurc_wspeed > hurc_dict.setdefault('max_wind_speed', 0):
                hurc_dict['max_wind_speed'] = hurc_wspeed

            hurc_pressure = float(line_fields[7][:-1])
            if hurc_pressure == -999:
                if 'minimum_pressure' not in hurc_dict.keys():
                    hurc_dict['minimum_pressure'] = None
                if 'maximum_pressure' not in hurc_dict.keys():
                    hurc_dict['maximum_pressure'] = None
            else:
                if not hurc_dict.setdefault('minimum_pressure'):
                    hurc_dict['minimum_pressure'] = hurc_pressure
                elif hurc_pressure < hurc_dict['minimum_pressure']:
                    hurc_dict['minimum_pressure'] = hurc_pressure
                if not hurc_dict.setdefault('maximum_pressure'):
                    hurc_dict['maximum_pressure'] = hurc_pressure
                elif hurc_pressure > hurc_dict['maximum_pressure']:
                    hurc_dict['maximum_pressure'] = hurc_pressure

            line = infile.readline()

        if line_fields[0][0].isalpha():
            break

    return hurc_dict, internal_last_pos


def main(filename):
    dict_list = list()
    with open(filename, 'r', newline='') as infile:
        last_pos = infile.tell()
        line = infile.readline()
        while line:
            line_fields = line.split()
            if line_fields[0][0].isalpha():
                hurc_results = list(hurc_handler(infile, last_pos))
                dict_list.append(hurc_results[0])
                last_pos = hurc_results[1]
            line = infile.readline()

# debugging
    for i in range(5):
        print(dict_list[i])


main('hurdat2-atlantic.txt')