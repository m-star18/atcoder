d = input()
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if d == day[0] or d == day[6]:
    print(0)
else:
    print(6 - day.index(d))
