t = int(input())

for i in range(t):

    n = input().split(":")
    # print("n: ", n)

    am_or_pm = "AM"

    hour = int(n[0])
    minute =  int(n[1])

    if hour >= 12:
        if hour == 12:
            am_or_pm = "PM"
        elif hour > 12:
            am_or_pm = "PM"
            hour -= 12
    
    if hour < 12 and am_or_pm == "AM":
        if hour + 12 <= 12:
            hour += 12
            am_or_pm = "AM"

    if len(str(hour)) < 2:
        hour = "0" + str(hour)

    if len(str(minute)) < 2:
        minute = "0" + str(minute)

    ans = str(hour) + ":" + str(minute)

    print(ans, am_or_pm)
