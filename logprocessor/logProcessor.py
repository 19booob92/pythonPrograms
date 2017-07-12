import re
import datetime
import sys
from utils import extractTime
from utils import ErrorDescription
from utils import findDate
from utils import isEmptyLine
from utils import isRegularStackTraceLine
from utils import parseDate
from utils import isInfoLineAfterStackTraceLine
from colorama import init
from colorama import Fore, Back, Style

# init colors
init()

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
rootError = ''
causedBy = ''
date = ''
prevLine = ''
for line in log:
    if isEmptyLine(line) or ('ERROR' in rootError and 'ERROR' not in line) or isInfoLineAfterStackTraceLine(line, prevLine):
        errDesc = ErrorDescription(causedBy, rootError, date, error);
        errors.append(errDesc)
        error = ''
        rootError = ''
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
        if 'ERROR' in rootError and 'ERROR' in line:
            rootError += line
        else:
            rootError = line


    if findDate(line) != None:
        date = findDate(line)

    prevLine = line

if dateToFind is not None:
    delta = datetime.timedelta(minutes = margin)
    time = extractTime(dateToFind)
    tmpTime = datetime.datetime.combine(datetime.date(1,1,1), time)
    timeFrom = (tmpTime - delta).time()
    timeTo = (tmpTime + delta).time()

def printColored(text, data):
    if (data is not None and len(data) > 0):
        print(text + Style.RESET_ALL, data)

for stacktrace in errors:
    timeFromError = parseDate(stacktrace.date)
    if dateToFind is None or (timeFromError <= timeTo and timeFromError >= timeFrom):
       printColored(Fore.RED + 'CAUSE : \n', stacktrace.cause)
       printColored(Fore.BLUE + 'DATE : \n', stacktrace.date)
       printColored(Fore.RED + 'ERROR : \n', stacktrace.error)
       printColored(Fore.RED + 'SERVICE :\n' , stacktrace.root)
       printColored(Fore.BLUE + 'PRIORITY: \n ', stacktrace.priority)
       print()
       print('*****************************************')

log.close()
