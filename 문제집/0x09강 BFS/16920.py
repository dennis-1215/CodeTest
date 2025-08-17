# https://www.acmicpc.net/problem/16920

from collections import deque
import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
speed = [0] + list(map(int, input().split()))
board = [list(input().strip()) for _ in range(N)]
answer = [0] * (P+1)

# 각 플레이어별 큐
queues = [deque() for _ in range(P+1)]

# 초기화
for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            continue
        elif board[i][j] == '.':
            continue
        else:
            uid = int(board[i][j])
            queues[uid].append((i, j))
            answer[uid] += 1

directions = [(-1,0), (1,0), (0,-1), (0,1)]

# 확장
while True:
    moved = False
    for uid in range(1, P+1):
        s = speed[uid]
        q = queues[uid]
        if not q:
            continue

        # BFS 레벨 단위로 s번 확장
        for _ in range(s):
            if not q:
                break
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '.':
                        board[nr][nc] = str(uid)
                        answer[uid] += 1
                        q.append((nr, nc))
                        moved = True

    if not moved:
        break

print(*answer[1:])




