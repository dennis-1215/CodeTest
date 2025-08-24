N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []
use = [False] * N
def dfs(n):
    if len(arr) == M:
        print(*arr)

    for i in range(n, N):
        if use[i]:
            continue

        arr.append(nums[i])
        use[i] = True
        dfs(i+1)
        use[i] = False
        arr.pop()

dfs(0)