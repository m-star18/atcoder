# sys.stdin.readline()
import sys
input = sys.stdin.readline

s = input()
mi, si = s.find('WWBWBWBWW'), s.find('WWBWBWW')
ans = ['Si','La','La','So','So','Fa','Fa','Mi','Re','Re','Do','Do','Si','La','La','So','So','Fa','Fa','Mi']
if si == -1:
    print(ans[19-mi])
else:
    print(ans[si])
