import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
n_a, n_b, n_c = 0, 0, 0
ans = 0

if a == b == c and a % 2 == 0:
    print(-1)
    exit()

elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    for i in range(10 ** 5):
        n_a = b // 2 + c // 2
        n_b = a // 2 + c // 2
        n_c = a // 2 + b // 2

        if n_a % 2 == 0 and n_b % 2 == 0 and n_c % 2 == 0:
            ans += 1
        else:
            ans += 1
            break

        a = n_a
        b = n_b
        c = n_c

print(ans)
