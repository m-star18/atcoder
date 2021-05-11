h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(h):
    for j in range(w):
        check = 0
        if s[i][j] == '#':
            if i != 0:
                if s[i - 1][j] == '#':
                    check += 1
            if j != 0:
                if s[i][j - 1] == '#':
                    check += 1
            if i != (h - 1):
                if s[i + 1][j] == '#':
                    check += 1
            if j != (w - 1):
                if s[i][j + 1] == '#':
                    check += 1
            if check == 0:
                print('No')
                exit()
print('Yes')
