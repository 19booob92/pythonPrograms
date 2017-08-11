import re
import sys 

invalidObjects = {}

def processLogLine(line):
        result = re.search('\[.*[0-9]{1,1000}', line)
        if (result is not None):
                splittedResult = result.group(0).split('.')
                classWithId = splittedResult[-1]
                className = classWithId.split('#')[0]
                objectId = classWithId.split('#')[1]
                if className in invalidObjects:
                        invalidObjects[className].append(objectId)
                else:
                        invalidObjects[className] = [objectId]

if sys.argv > 1:
        fileNames = list(sys.argv[1:])
        for name in fileNames:
                with open(name, 'r') as log:
                        for line in log:
                                if 'Caused by' in line and 'No row with the given identifier exists' in line:
                                        processLogLine(line)

for key in invalidObjects:
        print(key + ':')
        for val in set(invalidObjects[key]):
                print ('\t' + val)
