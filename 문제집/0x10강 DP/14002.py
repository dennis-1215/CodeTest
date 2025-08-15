# https://www.acmicpc.net/problem/14002

N = int(input())
A = list(map(int, input().split()))

DP = [1] * N
parent = [-1] * N

for i in range(N):
    for j in range(0, i):
        if A[j] < A[i] and DP[j] + 1 > DP[i]:
            DP[i] = DP[j]+1
            parent[i] = j

lis = max(DP)
print(lis)

idx = DP.index(lis)

track = []
while idx != -1:
    track.append(A[idx])
    idx = parent[idx]

track.reverse()
print(*track)