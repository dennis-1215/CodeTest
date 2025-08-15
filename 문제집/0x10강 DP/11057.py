# https://www.acmicpc.net/problem/11057

N = int(input())
DP = [[0] * 10 for _ in range(N+1)]

DP[1] = [1 for i in range(10)]

for i in range(2, N+1):
    for k in range(10):
        DP[i][k] = sum(DP[i-1][k:])

print(sum(DP[N]) % 10007)