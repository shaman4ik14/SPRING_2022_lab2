import json
import pprint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
args = parser.parse_args()

with open(args.path, 'r', encoding='utf-8') as file:
    data = json.load(file)

data_step = [data]


def dict_info(dict_data: dict):
    """
    Give all possible key from dict(like action 'ls')
    :param dict_data: dict
    :return: all key
    """
    for dict_key in dict_data.keys():
        print(f'    {dict_key}')


key_info = '"ls" - to see dict keys\n' \
           '"cd .." - to return to previous step\n' \
           '"type()" - to see the type of the current part of json\n' \
           '"command_info" - to see all possible commands\n' \
           '"current_part" - to see current part of json\n'\
           '"stop_search" - to stop viewing json'

while True:
    if len(data_step) >= 1:
        data = data_step[-1]
        if type(data) == list:
            key = input('Please enter key: ')
            if key == 'ls':
                print('command "ls" doesn`t exists in list')
            elif key == 'cd ..':
                if len(data_step) > 1:
                    data_step = data_step[:-1]
                else:
                    print('previous step doesn`t exist')
            elif key == 'type()':
                print(type(data))
            elif key == 'stop_search':
                break
            elif key == "command_info":
                print(key_info)
            elif key == "current_part":
                pprint.pprint(data)
            else:
                try:
                    if 0 <= int(key) < len(data):
                        data_step.append(data[int(key)])
                    else:
                        print('Key is wrong')
                except:
                    print(f'Key is wrong. Possible key is (0 - {len(data) - 1})')

        elif type(data) == dict:
            key = input('Please enter here: ')
            if key == 'ls':
                dict_info(data)
            elif key == 'cd ..':
                if len(data_step) > 1:
                    data_step = data_step[:-1]
                else:
                    print('previous step doesn`t exist')
            elif key == "command_info":
                print(key_info)
            elif key == 'stop_search':
                break
            elif key == "current_part":
                pprint.pprint(data)
            elif key == 'type()':
                print(type(data))
            elif key in data.keys():
                data_step.append(data[key])
            else:
                print('this key doesn`t exist')

        else:
            key = input('Please enter here: ')
            if key == 'ls':
                print('You reach end of json')
                print(f'Result of search is: {data}')
                break
            elif key == 'cd ..':
                if len(data_step) > 1:
                    data_step = data_step[:-1]
                else:
                    print('previous step doesn`t exist')
            elif key == 'type()':
                print(type(data))
            elif key == "command_info":
                print(key_info)
            elif key == "current_part":
                pprint.pprint(data)
            elif key == 'stop_search':
                break
            else:
                print(f'Result of search is: {data}')
    else:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data_step = [data]
