N, M = map(int, input().split())
pattern = [list(map(int, input().split())) for _ in range(N)]

MAX_VAL = max(max(row) for row in pattern)
nums = [0] * (MAX_VAL + 1)

for i in range(N):
    for j in range(M):
        nums[pattern[i][j]] += 1

odd_cnt, even_cnt = 0, 0
even_num_cnt = 0

for i in range(len(nums)):
    if nums[i] == 0:
        continue
    if nums[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
        even_num_cnt += nums[i]

if M % 2 == 0:
    if odd_cnt > 0:
        print("NO")
    else:
        print("YES")

elif M == 1:
    print("YES")

else:
    if odd_cnt > N or even_num_cnt < N or even_num_cnt % 2 != N % 2:
        print("NO")
    else:
        print("YES")
