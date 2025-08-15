# https://www.acmicpc.net/problem/12852
'''
1. X가 3으로 나누어 떨어지면 3으로 나누기
2. X가 2로 나누어 떨어지면 2로 나누가
3. 1을 빼기

N이 주어지면 세 개의 연산을 최소한으로 사용해서 1을 만들때 연산의 최솟값은?
'''

N = int(input())
INF = float('inf')
DP = [INF]*(N+1)
DP[1] = 0
parent = [0] * (N+1)

for i in range(1, N+1):
    if i * 3 <= N:
        if DP[i] + 1 < DP[i*3]:
            DP[i*3] = DP[i]+1
            parent[i*3] = i
    if i * 2 <= N:
        if DP[i] + 1 < DP[i * 2]:
            DP[i * 2] = DP[i] + 1
            parent[i * 2] = i
    if i + 1 <= N:
        if DP[i] + 1 < DP[i + 1]:
            DP[i + 1] = DP[i] + 1
            parent[i + 1] = i

print(DP[N])
path = []
while N:
    path.append(N)
    N = parent[N]
print(*path)