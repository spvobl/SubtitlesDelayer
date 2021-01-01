import re
from datetime import datetime, timedelta


def time(timeString, addTimeString):
    try:
        timeObj = datetime.strptime("2020 " + timeString, '%Y %H:%M:%S,%f')
        addSecond, addMilliSecond = addTimeString.split(".")
    except:
        return timeString
    return (timeObj + timedelta(seconds=int(addSecond), milliseconds=int(addMilliSecond))).strftime("%H:%M:%S,%f")


def subDelay(subFileName, newFileName, addTime):
    #subFileTxt = open('subFile.srt', "r").read()
    subFileTxt = open(subFileName, "r").read()
    #newFile = open('newFile.srt', "w")
    newFile = open(newFileName, "w")
    #addTime = "-47.200"
    timeArr = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}', subFileTxt)
    for x in timeArr:
        subFileTxt = subFileTxt.replace(x, time(x, addTime))
    newFile.write(subFileTxt)
    newFile.close()
