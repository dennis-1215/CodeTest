# https://www.acmicpc.net/problem/15683
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

directions = [[],
              [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
              [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
              [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
              [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1,0), (0, -1), (-1, 0)]],
              [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
              ]
def blind_check(arr):
    visited = [[False] * M for _ in range(N)]

    for (r, c), cctv, d in arr:
        for dx, dy in directions[cctv][d]:
            nx, ny = r, c
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < N and 0 <= ny < M):
                    break
                if office[nx][ny] == 6:
                    break
                if office[nx][ny] == 0:
                    visited[nx][ny] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and office[i][j] == 0:
                cnt += 1

    return cnt

cctv = []
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv.append([(i,j), office[i][j], 0])


arr = []
answer = float('inf')

def dfs(i):
    global answer
    if i == len(cctv):
        answer = min(answer, blind_check(arr))
        if answer == 0:
            print(0)
            exit()
        return

    pos, cctv_num, _ = cctv[i]
    for d in range(len(directions[cctv_num])):
        arr.append([pos, cctv_num, d])
        dfs(i + 1)
        arr.pop()

dfs(0)
print(answer)