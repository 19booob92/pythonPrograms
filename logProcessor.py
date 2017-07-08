import re
import datetime

HIGH = '/\\'
MID = '--'
LOW = '\/'
class ErrorDescription:
    def __init__(self, cause, root, date, error):
        self.cause = cause
        self.root = root
        self.date = date
        self.error = error
        self.priority = self.findPriority()

    def findPriority(self):
        if 'hibernate' in self.cause or 'hibernate' in self.root:
            return HIGH
        elif 'gwt' in self.cause.lower():
            return LOW
        else:
            return MID

def isEmptyLine(line):
    if '\n' in line and len(line) < 2:
        return True
    else:
        return False

rootPackage = 'intenso'
def isRegularStackTraceLine(line):
    if line.startswith('\t'):
        return True
    return False

def findDate(line):
 result = re.search('[a-z]{3} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}', line)
 if result == None:
     return None
 else:
     return result.group(0)

def extractTime(stringDate):
    splittedDate = stringDate.split(':')
    time = datetime.time(int(splittedDate[0]), int(splittedDate[1]), int(splittedDate[2]))
    return time

def parseDate(stringDate):
    if not isEmptyLine(stringDate):
        splittedStringDate = stringDate.split(' ')
        time = extractTime(splittedStringDate[3])
        return time

log = open('localhost.2017-02-20.log')

errors = []

error = ''
prevLine = ''
causedBy = ''
date = ''
for line in log:
    if isEmptyLine(line):
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
        prevLine = line


    if findDate(line) != None:
        date = findDate(line)


dateToFind = '2:0:0'
delta = datetime.timedelta(minutes = 5)
time = extractTime(dateToFind)
tmpTime = datetime.datetime.combine(datetime.date(1,1,1), time)
timeFrom = (tmpTime - delta).time()
timeTo = (tmpTime + delta).time()

for stacktrace in errors:
    timeFromError = parseDate(stacktrace.date)
    if timeFromError <= timeTo and timeFromError >= timeFrom:
       print('CAUSE : \n', stacktrace.cause)
       print('DATE : \n', stacktrace.date)
       print('ERROR : \n', stacktrace.error)
       print('SERVICE :\n' , stacktrace.root)
       print('PRIORITY: \n ', stacktrace.priority)
       print()
       print('*****************************************')

