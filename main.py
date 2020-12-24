
import re

def time(timeString, addTimeString):
    hour, minute, second, milliSecond = re.split(":|,", timeString)
    addTime = re.split(".", addTimeString)
    

if __name__ == "__main__":
    time("00:34:13,234", "8.345")
    time("00:34:13,234", "-8.345")
