#!/usr/bin/env python3

from operator import itemgetter
import sys

current_key = None
current_value = 0
key = None
for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_key == key:
        current_value += count
    else:
        if current_key:
            print ('%s\t%s' % (current_key, current_value))
        current_key = key
        current_value = count
if current_key == key:
    print ('%s\t%s' % (current_key, current_value))
