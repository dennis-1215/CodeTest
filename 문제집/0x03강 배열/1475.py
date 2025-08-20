N = list(map(int, input().strip()))

nums = [0] * 9

for i in range(9):
    nums[i] += N.count(i)
    if i == 6:
        nums[i] += N.count(9)
        nums[i] = (nums[i] + 1) // 2

print(max(nums))