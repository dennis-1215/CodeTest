# https://www.acmicpc.net/problem/14442
from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]
for i in range(K+1):
    visited[i][0][0] = True

q = deque([(1, 0, 0, 0)])
while q:
    moves, k, r, c = q.popleft()

    if (r, c) == (N-1, M-1):
        print(moves)
        exit()

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] == 1 and k < K and not visited[k+1][nr][nc]:
                visited[k+1][nr][nc] = True
                q.append((moves+1, k+1, nr, nc))

            if grid[nr][nc] == 0 and not visited[k][nr][nc]:
                visited[k][nr][nc] = True
                q.append((moves + 1, k, nr, nc))

print(-1)