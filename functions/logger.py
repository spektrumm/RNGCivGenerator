
from datetime import datetime
import os
import os.path


def createLogFile():
    cwd = os.getcwd()
    logDir = os.path.join(cwd, 'logs')
    if os.path.exists(logDir):
        pass
    else:
        os.mkdir(logDir)
    now = datetime.now()
    currentTime = now.strftime("%H-%M-%S")

    logName = f'{logDir}\\LOG-({currentTime}).txt'
    with open(logName, 'w') as f:
        f.write(f'BEGIN LOG {currentTime}\n')

    return logName


def logMsg(content, logName):
    now = datetime.now()

    with open(logName, 'a') as f:
        f.write(f'LOG({now}): {content}\n')


def printMsg(content):
    now = datetime.now()
    print(f'LOG({now}): {content}\n')
