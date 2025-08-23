import sys
input = sys.stdin.readline

N = int(input())

heights = []
for _ in range(N):
    heights.append(int(input()))

stack = []
answer = 0
for i in range(N):
    h = heights[i]

    # 현재 빌딩 다음이 더 높은 빌딩이면 이 빌딩은 이제 관측 못함
    while stack and stack[-1] <= h:
        stack.pop()

    # 현재 빌딩은 나보다 큰 이전의 빌딩들 개수 만큼 관측됨
    answer += len(stack)

    # 현재 빌딩을 스택에 추가
    stack.append(h)

print(answer)