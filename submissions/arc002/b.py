import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from datetime import datetime, timedelta

fmt = '%Y/%m/%d'
date = datetime.strptime(readline().rstrip().decode(), fmt)
while 1:
    y, m, d = date.year, date.month, date.day
    if y % (m * d) == 0:
        break
    date += timedelta(days=1)
print(date.strftime(fmt))
