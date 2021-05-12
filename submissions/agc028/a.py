import fractions


def binary_search(list, number, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid][0]
        if guess == number:
            if list[mid][1] == item:
                return False
            else:
                return True
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
    # 見つからなかったとき
    return False


n, m = map(int, input().split())
s = input()
t = input()
check = []
l = n * m // fractions.gcd(n, m)
for i in range(n):
    check.append([i * l // n, s[i]])
for i in range(m):
    if binary_search(check, i * l // m, t[i]):
        print(-1)
        exit()
print(l)
