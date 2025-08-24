N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = dict()

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
        arr.append(nums[i])
        dfs(i)
        arr.pop()

dfs(0)