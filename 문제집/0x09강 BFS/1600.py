# https://www.acmicpc.net/problem/1600
from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())

monkey = [(-1, 0), (1, 0), (0, -1), (0, 1)]
horse = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

grid = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False] * W for _ in range(H)] for _ in range(K+1)]

for i in range(K+1):
    visited[i][0][0] = True
q = deque([(0, 0, 0, 0)])

while q:
    moves, k, r, c = q.popleft()

    if (r, c) == (H-1, W-1):
        print(moves)
        exit()

    if k < K:
        for dr, dc in horse:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and not visited[k+1][nr][nc] and grid[nr][nc] == 0:
                visited[k+1][nr][nc] = True
                q.append((moves+1, k+1, nr, nc))

    for dr, dc in monkey:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and not visited[k][nr][nc] and grid[nr][nc] == 0:
            visited[k][nr][nc] = True
            q.append((moves + 1, k, nr, nc))

print(-1)

'''
2
8 12
0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 0 0 0 0 0
0 1 1 0 1 1 1 1
0 1 1 0 1 1 1 1
0 1 1 0 0 0 0 0
0 1 1 0 1 1 1 0
0 1 1 1 1 1 1 0
1 1 0 0 0 0 1 1
1 1 1 1 1 1 1 1
1 1 1 0 1 1 0 0
-> 14

1
7 8
0 0 0 0 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 0
0 0 0 1 1 1 0
0 1 1 1 0 0 0
0 1 1 1 1 1 1
0 1 1 1 1 1 1
0 0 0 0 0 0 0
'''