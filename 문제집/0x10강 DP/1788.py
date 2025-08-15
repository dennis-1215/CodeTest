# https://www.acmicpc.net/problem/1788

N = int(input())
DP = [0] * 1000001

DP[0] = 0
DP[1] = 1
DP[2] = 1

for i in range(3, 1000001):
    DP[i] = (DP[i-1]+DP[i-2]) % 1000000000

if N < 0:
    if N % 2 == 0:
        print(-1)
    else:
        print(1)
    print(DP[abs(N)])

else:
    if N == 0:
        print(0)
    else:
        print(1)

    print(DP[N])