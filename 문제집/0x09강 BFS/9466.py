# https://www.acmicpc.net/problem/9466
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(v, mark):
    visited[v] = mark
    nxt = graph[v]

    if visited[nxt] == 0:
        dfs(nxt, mark)

    elif visited[nxt] == mark: # 사이클
        u = nxt
        while True:
            team_cnt[0] += 1
            u = graph[u]
            if u == nxt:
                break

    print(visited)
    print()

for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))

    visited = [0] * (N+1)
    team_cnt = [0]
    mark = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            mark+=1
            dfs(i, mark)

    print(N-team_cnt[0])