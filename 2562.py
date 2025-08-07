# https://www.acmicpc.net/problem/2562

max_num, index = 0, 0

for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        index = i

print(max_num)
print(index)