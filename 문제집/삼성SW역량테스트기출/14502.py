# https://www.acmicpc.net/problem/14502
'''
바이러스가 퍼지는데 벽을 3개 쳐서 최대한 안퍼지게 하기
즉, 안전구역을 최대한 많이 확보하도록 벽을 치는 문제다.

벽 3개를 빈칸에 놓을 수 있는 경우는 조합(Combination)을 통해 구할 수 있다.
빈칸 배열에서 3개를 고르는 조합에 대해서
바이러스를 퍼트린 뒤 0의 개수를 구하고 최대값을 업데이트 하면 된다.

'''
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

blanks = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
viruses = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

def virus_bfs(board):
    q = deque(viruses)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

def count_safe_area(board):
    return sum(cell == 0 for row in board for cell in row)

answer = 0

for w1, w2, w3 in combinations(blanks, 3):
    copy_lab = copy.deepcopy(lab)

    for x, y in (w1, w2, w3):
        copy_lab[x][y] = 1

    virus_bfs(copy_lab)
    answer = max(count_safe_area(copy_lab), answer)

print(answer)