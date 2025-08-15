# https://www.acmicpc.net/problem/2748

DP = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

for i in range(len(DP), 91):
    DP.append(DP[i-1] + DP[i-2])

N = int(input())
print(DP[N])