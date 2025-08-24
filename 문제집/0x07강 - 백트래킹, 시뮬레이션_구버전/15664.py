N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = dict()
used = [False] * N

arr = []
def dfs(n):
    global arr

    if len(arr) == M:
        if tuple(arr) in visited:
            return
        print(*arr)
        visited[tuple(arr)] = 1
        return


    for i in range(n, N):
        if used[i]:
            continue

        arr.append(nums[i])
        used[i] = True
        dfs(i+1)
        used[i] = False
        arr.pop()

dfs(0)