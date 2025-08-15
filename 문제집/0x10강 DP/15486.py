# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline
N = int(input())

DP = [0] * (N+2)
schedule = [[]]
for _ in range(N):
    schedule.append(list(map(int, input().split())))

for i in range(N, 0, -1):
    date, pay = schedule[i]
    if i+date <= N+1:
        DP[i] = max(DP[i+1], DP[i+date] + pay)
    else:
        DP[i] = DP[i+1]

print(DP[1])