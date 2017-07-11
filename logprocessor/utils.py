import re
import datetime
import sys

HIGH = '/\\'
MID = '--'
LOW = '\/'


def isEmptyLine(line):
    if '\n' in line and len(line) < 2:
        return True
    else:
        return False

def isRegularStackTraceLine(line):
    if line.startswith('\t'):
        return True
    return False


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

def findDate(line):
    result = re.search(' [0-9]{1,2}:[0-9]{1,2}:[0-9i]{1,2}', line)
    if result == None:
        return None
    else:
        return result.group(0)[1:]

def parseDate(stringDate):
    if not isEmptyLine(stringDate) and len(stringDate) > 0:
        time = extractTime(stringDate)
        return time
    return None

def extractTime(stringDate):
    splittedDate = stringDate.split(':')
    time = datetime.time(int(splittedDate[0]), int(splittedDate[1]), int(splittedDate[2]))
    return time
