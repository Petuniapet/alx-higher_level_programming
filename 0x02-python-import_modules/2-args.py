#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

print("{} argument{}:".format(argc, 's' if argc != 1 else ''))

for i, arg in enumerate(argv[1:], 1):
    print("{}: {}".format(i, arg))
