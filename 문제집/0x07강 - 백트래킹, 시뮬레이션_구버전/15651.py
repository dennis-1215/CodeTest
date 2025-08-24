N, M = map(int, input().split())

arr = []
def dfs():
    global arr

    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N+1):
        arr.append(i)
        dfs()
        arr.pop()

dfs()