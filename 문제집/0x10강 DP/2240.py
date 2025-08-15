# https://www.acmicpc.net/problem/2240
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
DP = [[0] * (W+1) for _ in range(T+1)]

plums = [0]
for i in range(T):
    plums.append(int(input()))

for t in range(1, T+1):
    for m in range(W+1):
        pos = 1 if m % 2 == 0 else 2

        if m == 0:
            DP[t][m] = DP[t-1][m] + (plums[t] == pos)
        else:
            DP[t][m] = max(DP[t - 1][m], DP[t - 1][m - 1]) + (plums[t] == pos)

print(max(DP[T]))