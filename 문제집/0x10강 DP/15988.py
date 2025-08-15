T = int(input())

DP = [0] * 1000001

DP[1] = 1
DP[2] = 2
DP[3] = 4
DP[4] = 7

for i in range(5, 1000001):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009

for _ in range(T):
    N = int(input())
    print(DP[N])