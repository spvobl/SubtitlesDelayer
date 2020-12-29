import re
from datetime import datetime, timedelta
def time(timeString, addTimeString):
    try:
        timeObj = datetime.strptime(timeString, '%H:%M:%S,%f')
        addSecond, addMilliSecond = addTimeString.split(".")
    except:
        return timeString
    return (timeObj + timedelta(seconds = int(addSecond), milliseconds = int(addMilliSecond) )).strftime("%H:%M:%S,%f")

if __name__ == "__main__":
    subFileTxt = open('subFile.srt',"r", encoding='utf-8').read()
    newFile = open('newFile.srt',"w", encoding='utf-8')
    addTime = "-43.234"
    timeArr = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}',subFileTxt)
    for x in timeArr:
        subFileTxt = subFileTxt.replace(x,time(x,addTime))
    newFile.write(subFileTxt)
    newFile.close()
