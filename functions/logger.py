# logging functions for debugging and error catching


from datetime import datetime
import os
import os.path

# creates a log file and ensures a log folder exists


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


# logs message <content> to the log file <logName>


def logMsg(content, logName):
    now = datetime.now()

    with open(logName, 'a') as f:
        f.write(f'LOG({now}): {content}\n')


# prints message <content> to the console


def printMsg(content):
    now = datetime.now()
    print(f'LOG({now}): {content}\n')
