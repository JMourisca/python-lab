def timeConversion(s):
    time = s[0:8]
    ampm = s[-2:]

    if time[0:2] == "12" and ampm == "AM":
        return "00" + time[2:]
    elif time[0:2] == "12" and ampm == "PM":
        return "12" + time[2:]

    if ampm == "AM":
        return time
    else:
        return str((int(time[0:2]) + 12)) + time[2:]


print(timeConversion("07:05:45PM"))
print(timeConversion("07:05:45AM"))
print(timeConversion("12:00:00AM"))
print(timeConversion("12:05:00AM"))
print(timeConversion("12:05:00PM"))