import  sys
input = sys.stdin.readline

n = int(input())
h = n//3600
m = (n-3600*h)//60
s = (n-3600*h-(60*m))
times = [h, m, s]
ans = []
for i in range(3):
    if times[i] < 10:
        ans.append('0'+str(times[i]))
    else:
        ans.append(str(times[i]))
print(ans[0]+':'+ans[1]+':'+ans[2])
