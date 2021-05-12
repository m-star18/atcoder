import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))


def merge_sort(lst):
    memory = [None] * len(lst)
    begin = 0
    end = len(lst) - 1
    _merge_sort(lst, memory, begin, end)


def _merge_sort(lst, memory, begin, end):
    if begin == end:
        return

    mid = begin + (end - begin) // 2
    _merge_sort(lst, memory, begin, mid)
    _merge_sort(lst, memory, mid + 1, end)

    for i in range(begin, end + 1):
        memory[i] = lst[i]

    left, index, right = begin, begin, mid + 1
    while (left <= mid) and (right <= end):
        if memory[left] <= memory[right]:
            lst[index] = memory[left]
            left = left + 1
        else:
            lst[index] = memory[right]
            right = right + 1
        index = index + 1

    while left <= mid:
        lst[index] = memory[left]
        left = left + 1
        index = index + 1

    while right <= mid:
        lst[index] = memory[right]
        right = right + 1
        index = index + 1


ans = a + b
merge_sort(ans)
print(*ans)
