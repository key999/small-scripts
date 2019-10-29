#!/usr/bin/env python3

# Python 3.5.2 (default, Oct 25 2016, 15:13:01) 
# [GCC 5.4.0 20160609] on linux

# a simple timer, nothing to add
# works with stdout to clear bottom output line and keep the time in one line

from time import sleep
from sys import stdout

try:
    def start(hr, mins, sec):
        time = hr*3600 + mins*60 + sec
        print("That's", hr, "hours,", mins, "minutes,", sec, "seconds.")
        input('Press Enter to start...')
        backspace = 8 * "\b" + "\r"
        pom = None

        while time >= 0:
            if hr < 10:
                pom = str(hr)
                hr_s = str("0" + pom)
            else:
                hr_s = str(hr)
            if mins < 10:
                pom = str(mins)
                mins_s = str("0" + pom)
            else:
                mins_s = str(mins)
            if sec < 10:
                pom = str(sec)
                sec_s = str("0" + pom)
            else:
                sec_s = str(sec)

            print(backspace, hr_s, ':', mins_s, ':', sec_s, sep="", end="", flush=True)
            if sec == 0 and mins != 0 and hr != 0:
                # HH:MM:00
                sec = 59 ; mins -= 1
            elif sec == 0 and mins == 0 and hr != 0:
                # HH:00:00
                sec = 59 ; mins = 59 ; hr -= 1
            elif sec == 0 and mins != 0 and hr == 0:
                # 00:MM:00
                sec = 59 ; mins -= 1
            elif sec != 0 and mins == 0 and hr == 0:
                # 00:00:SS
                sec -= 1
            elif sec != 0 and mins == 0 and hr != 0:
                # HH:00:SS
                sec -= 1
            elif sec != 0 and mins != 0 and hr == 0:
                # 00:MM:SS
                sec -= 1
            elif sec != 0 and mins != 0 and hr != 0:
                # HH:MM:SS
                sec -= 1
            time -= 1
            sleep(1
                    )
        print("\nTime is up")

    try:
        print("Try not to exceed 99 hours")
        hr = int(input('Hours - '))
    except ValueError:
        hr = 0
    try:
        mins = int(input('Minutes - '))
        if mins >= 60:
            hr += mins // 60
            mins = mins % 60
    except ValueError:
        mins = 0
    try:
        sec = int(input('Seconds - '))
        if sec >= 60 and sec < 3600:
            mins += sec // 60
            sec = sec % 60
        elif sec >= 3600:
            hr += sec // 3600
            sec = sec % 3600
            mins += sec // 60
            sec = sec % 60
    except ValueError:
        sec = 0

    if hr == mins == sec == 0:
        print("Nothing to do here, exiting")
    else:
        start(hr, mins, sec)

except KeyboardInterrupt:
    print("\nStopped")
