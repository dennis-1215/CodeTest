# https://www.acmicpc.net/problem/15684
'''


'''

import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[False] * (N+1) for _ in range(H+1)]

# 가로선 정보 저장 (입력 인덱스 수정)
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = True

# 사다리 게임 시뮬레이션
def simulate():
    for start in range(1, N+1):
        k = start
        for h in range(1, H+1):
            if ladder[h][k]:
                k += 1
            elif k > 1 and ladder[h][k-1]:
                k -= 1
        if k != start:
            return False
    return True

answer = 4  # 0~3까지 가능, 4면 불가능

def dfs(count, x, y):
    global answer
    # 이미 더 나쁜 경우
    if count >= answer:
        return
    # 조건 만족 시 최소값 갱신
    if simulate():
        answer = count
        return
    # 3개까지 가능
    if count == 3:
        return

    for i in range(x, H+1):
        k = y if i == x else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(count+1, i, j+2)  # 인접 칸은 건너뛰기
                ladder[i][j] = False

# 백트래킹 시작
dfs(0, 1, 1)
print(answer if answer < 4 else -1)
