N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = []
for i in range(N):
    while stack and stack[-1][1] < A[i]:
        idx, num = stack.pop()
        answer[idx] = A[i]

    stack.append((i, A[i]))

print(*answer)