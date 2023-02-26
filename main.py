import tkinter as tk
from tkinter import filedialog
import re
from decimal import Decimal
import os
from inputData import get_input_data

def open_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def get_new_file_path(path):
    count = len(path) - 1
    while path[count] != '.':
        count -= 1
    return path[:count] + ' Mirrored' + path[count:]


def mirror_line(line, mirror_value):
    x = re.search("^G0 |^G1 ", line)
    if x is None:
        return line
    x = re.search(" X", line)
    if x is None:
        return line
    start_index = x.span()[1]
    count = start_index
    while count < len(line) and line[count] != " ":
        count += 1
    stop_index = count
    value = Decimal(line[start_index:stop_index])
    new_value = mirror_value - value
    new_line = line[:start_index] + str(new_value) + line[stop_index:]
    return new_line


def create_mirrored_file(path):
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    config_file_name = "mirror_value.txt"
    mirror_value = 550.0
    try:
        mirror_value_file = open(desktop + "\\" + config_file_name, 'r')
        mirror_value = Decimal(mirror_value_file.readline())
    except FileNotFoundError:
        mirror_value = Decimal(get_input_data(mirror_value))
        print(mirror_value)
        new_file = open(desktop + "\\" + config_file_name, 'w')
        new_file.write(str(mirror_value))
        new_file.close()
    print(mirror_value)
    new_file_path = get_new_file_path(path)
    destination_file = open(new_file_path, 'w')
    source_file = open(path, 'r')
    lines = source_file.readlines()
    for line in lines:
        new_line = mirror_line(line, mirror_value)
        destination_file.write(new_line)
    source_file.close()
    destination_file.close()


create_mirrored_file(open_file())
