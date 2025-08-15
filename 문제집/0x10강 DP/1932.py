# https://www.acmicpc.net/problem/1932

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, 0, -1):
    for j in range(i):
        triangle[i-1][j] = max(triangle[i-1][j]+triangle[i][j], triangle[i-1][j]+triangle[i][j+1] )

print(triangle[0][0])
