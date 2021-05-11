# sys.stdin.readline()
import sys
input = sys.stdin.readline

a, p = map(int, input().split())
ans = (3*a + p)//2
print(ans)
