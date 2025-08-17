import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(N)]

K = min(N, M)

answer = [0] * K

def check(r, c, num):
    if num == 0:
        if grid[r][c] == 'X':
            return True
        return False

    for i in range(num+1):
        for j in range(num+1):
            if i == j:
                if grid[r+i][c+j] == '.':
                    return False

            elif grid[r+i][c+j] == 'X':
                return False

    return True


for i in range(N):
    for j in range(M):
        if grid[i][j] == 'X':
            for k in range(K):
                if i+k >= N or j+k >= M:
                    break
                if check(i, j, k):
                    answer[k] += 1

for a in answer:
    print(a)

