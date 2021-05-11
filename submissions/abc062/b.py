h, w = map(int, input().split())
hw = '#'*(w+2)
a = []
for i in range(h):
    a.append(input())
print(hw)
for i in range(h):
    print('#'+a[i]+'#')
print(hw)
