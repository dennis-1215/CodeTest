# https://www.acmicpc.net/problem/6593

from collections import deque
import sys
input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        exit()

    building = []
    for _ in range(L):
        floor = []
        for _ in range(R):
            floor.append(list(map(str, input().strip())))

        building.append(floor)
        input()

    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    goal = 0
    q = deque()
    for f in range(L):
        for r in range(R):
            for c in range(C):
                if building[f][r][c] == 'S':
                    visited[f][r][c] = True
                    q.append((0, f, r, c))
                elif building[f][r][c] == 'E':
                    building[f][r][c] = '.'
                    goal = (f, r, c)

    flag = True
    while q:
        depth, floor, row, col = q.popleft()
        if (floor, row, col) == goal:
            print(f"Escaped in {depth} minute(s).")
            flag = False
            break

        for df, dr, dc in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0,0,-1), (0,0,1)]:
            nf, nr, nc = floor+df, row+dr, col+dc
            if 0 <= nf < L and 0 <= nr < R and 0 <= nc < C:
                if not visited[nf][nr][nc] and building[nf][nr][nc] == '.':
                    visited[nf][nr][nc] = True
                    q.append((depth+1, nf, nr, nc))

    if flag:
        print("Trapped!")
