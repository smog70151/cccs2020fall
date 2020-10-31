#!/usr/bin/env python3

import sys

def hash(key):
    monthDict = {}
    monthDict['Jan'] = '01'
    monthDict['Feb'] = '02'
    monthDict['Mar'] = '03'
    monthDict['Apr'] = '04'
    monthDict['May'] = '05'
    monthDict['Jun'] = '06'
    monthDict['Jul'] = '07'
    monthDict['Aug'] = '08'
    monthDict['Sep'] = '09'
    monthDict['Oct'] = '10'
    monthDict['Nov'] = '11'
    monthDict['Dec'] = '12'
    return monthDict[key]

for line in sys.stdin:
    line = line.strip()
    time = line.split('[')[1].split(']')[0]
    year = time.split('/')[2].split(':')[0]
    month = hash(time.split('/')[1])
    day = time.split('/')[0]
    hour = time.split('/')[2].split(':')[1]
    key = year + '-' + month + '-' + day + ' T ' + hour + ':00:00.000'
    print ('%s\t%s' % (key, 1))
