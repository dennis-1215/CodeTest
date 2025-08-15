# https://www.acmicpc.net/problem/2302

N = int(input())
M = int(input())

DP = [0] * 41

DP[1] = 1
DP[2] = 2
DP[3] = 3

for i in range(4, 41):
    DP[i] = DP[i-2] + DP[i-1]

seat = ['0'] * N

for _ in range(M):
    vip = int(input())
    seat[vip-1] = '1'

seat = ''.join(seat).split('1')

answer = 1
for s in seat:
    if s == '':
        continue
    answer *= DP[len(s)]

print(answer)

