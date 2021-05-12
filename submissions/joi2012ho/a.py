import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


def memo(ss):
    return 1 if ss == 'J' else 0, 0, 0


s = readline().rstrip().decode() + '.'
cnt, check, flag = memo('')
ans = 0
for ss in s:
    if flag == 0:
        if ss == 'J':
            cnt += 1
        else:
            if ss == 'O':
                flag = 1
                check = 1
            else:
                cnt = 0
    elif flag == 1:
        if ss == 'O':
            check += 1
        else:
            if ss == 'I' and cnt >= check:
                cnt = min(cnt, check)
                flag = 2
                check = 1
            else:
                cnt, check, flag = memo(ss)
    else:
        if ss == 'I':
            check += 1
        else:
            if cnt <= check:
                ans = max(ans, min(cnt, check))
            cnt, check, flag = memo(ss)
print(ans)
