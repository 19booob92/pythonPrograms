"""
 example log entry :
 TIME_TESTmetodaB-21 START 2
"""


import sys

logName = sys.argv[1]

times = {}

DELIMETER = ' '
PREFIX = 'TIME_TEST'
ID_DELIMETER = '-'


with open(logName) as log:
    for line in log:
        if (line.startswith(PREFIX)):
            params = line.split(DELIMETER)

            method_name = params[0].replace(PREFIX, '')
            start_or_stop = params[1]
            time = params[2].replace('\n', '')
            times[method_name + start_or_stop] = int(time)

result = {}
START_PREFIX = 'START'
STOP_PREFIX = 'STOP'

for time in times:
    if START_PREFIX in time:
        method_name = time.replace(START_PREFIX, '')
        start_date = times[time]
        end_date = times[method_name + STOP_PREFIX]
        result[method_name] = end_date - start_date

grouped = {}

for time in result:
    method_name = time.split('-')[0]
    if method_name in grouped.keys():
        grouped[method_name] = grouped[method_name] + result[time]
    else:
        grouped[method_name] = result[time]


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = result.keys()
y_pos = np.arange(len(objects))
performance = result.values()

fig = plt.figure()

plt.subplot(2,1,1)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')

objects = grouped.keys()
y_pos = np.arange(len(objects))
performance = grouped.values()

plt.subplot(2,1,2)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')


plt.show()

