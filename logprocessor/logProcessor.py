import re
import datetime
import sys
from utils import extractTime
from utils import ErrorDescription
from utils import findDate
from utils import isEmptyLine
from utils import isRegularStackTraceLine
from utils import parseDate

#handle help
if len(sys.argv) > 1 and sys.argv[1] == 'h':
    print('arg[0] : path to file \n arg[1] : time {hh:mm} \n arg[2] margin {mm}')

pathToFile = 'localhost.2017-02-20.log'
rootPackage = 'intenso'
dateToFind = '2:0:0'
margin = 5

if len(sys.argv) == 4:
    pathToFile = sys.argv[1]
    dateToFind = sys.argv[2] + ':00'
    margin = int(sys.argv[3])
else:
    pathToFile = sys.argv[1]
    dateToFind = None

errors = []

log = open(pathToFile)

error = ''
prevLine = ''
causedBy = ''
date = ''
for line in log:
    if isEmptyLine(line) or ('ERROR' in prevLine and 'ERROR' not in line):
        errDesc = ErrorDescription(causedBy, prevLine, date, error);
        errors.append(errDesc)
        error = ''
        prevLine = ''
        causedBy = ''

    if isRegularStackTraceLine(line):
        if rootPackage is not None and len(rootPackage) > 0:
            if rootPackage in line:
                error += line
                error = error.replace('\t', '')
    elif 'Caused by' in line or 'Pozycja' in line:
        causedBy += line
        causedBy = causedBy.replace('Caused by', '')
    elif 'Caused by' not in line and '...' not in line:
        if 'ERROR' in prevLine and 'ERROR' in line:
            prevLine += line
        else:
            prevLine = line


    if findDate(line) != None:
        date = findDate(line)

if dateToFind is not None:
    delta = datetime.timedelta(minutes = margin)
    time = extractTime(dateToFind)
    tmpTime = datetime.datetime.combine(datetime.date(1,1,1), time)
    timeFrom = (tmpTime - delta).time()
    timeTo = (tmpTime + delta).time()

for stacktrace in errors:
    timeFromError = parseDate(stacktrace.date)
    if dateToFind is None or (timeFromError <= timeTo and timeFromError >= timeFrom):
       print('CAUSE : \n', stacktrace.cause)
       print('DATE : \n', stacktrace.date)
       print('ERROR : \n', stacktrace.error)
       print('SERVICE :\n' , stacktrace.root)
       print('PRIORITY: \n ', stacktrace.priority)
       print()
       print('*****************************************')

log.close()
