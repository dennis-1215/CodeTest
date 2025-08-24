N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []
def dfs():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(nums[i])
        dfs()
        arr.pop()

dfs()