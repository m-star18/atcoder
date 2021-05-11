import itertools

abcd = input()
memo = list(itertools.product(['+', '-'], repeat=3))

for i in range(2 ** 3):
    cnt = int(abcd[0])
    for j in range(3):
        if memo[i][j] == '+':
            cnt += int(abcd[j + 1])
        else:
            cnt -= int(abcd[j + 1])
    if cnt == 7:
        print(abcd[0] + memo[i][0] + abcd[1] + memo[i][1] + abcd[2] + memo[i][2] + abcd[3] + '=7')
        break
