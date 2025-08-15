T = int(input())

DP = [[0, 0] for _ in range(41)]
DP[0] = [1, 0]
DP[1] = [0, 1]
DP[2] = [1, 1]

for i in range(3, 41):
    DP[i][0] = DP[i - 1][0] + DP[i - 2][0]
    DP[i][1] = DP[i - 1][1] + DP[i - 2][1]

for _ in range(T):
    N = int(input())
    print(*DP[N])
