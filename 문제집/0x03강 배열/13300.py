N, K = map(int, input().split())

SYarr = [[0]*7 for _ in range(2)]

for _ in range(N):
    s, y = map(int, input().split())
    SYarr[s][y] += 1

answer = 0
for arr in SYarr:
    for a in arr:
        if a == 0:
            continue
        answer += a//K
        if a % K > 0:
            answer += 1

print(answer)