import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []  # (번호, 높이)
answer = []

for i in range(N):
    h = heights[i]
    # 현재 탑보다 낮은 탑들은 신호를 못 받음 -> pop
    while stack and stack[-1][1] < h:
        stack.pop()

    if not stack:  # 왼쪽에 수신 가능한 탑이 없음
        answer.append(0)
    else:  # 스택 상단의 탑이 신호를 받음
        answer.append(stack[-1][0])

    stack.append((i + 1, h))  # 현재 탑 push (번호는 1부터 시작)

print(*answer)