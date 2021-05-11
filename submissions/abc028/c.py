# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, b, c, d, e = map(int, input().split())
ans = list(set([a+b+c,a+b+d,a+b+e,a+c+d,a+c+e,a+d+e,b+c+d,b+c+e,b+d+e,c+d+e]))
ans.sort(reverse=True)
print(ans[2])
