import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = 0
for _ in range(N):
    h = int(input())
    cnt = 1

    # 지금 사람이 top보다 키가 크다면 top의 사람(들)은 지금 사람 이후의 사람을 볼 수 없다.
    while stack and stack[-1][0] < h:
        answer += stack[-1][1]
        stack.pop()

    # 같은 키끼리는 서로 다 볼 수 있다. 2차원 배열로 (키, 인원수)로 저장한다.
    if stack and stack[-1][0] == h:
        same = stack.pop()
        answer += same[1]
        cnt = same[1] + 1

    # 바로 전에 사람이 있다면 그 사람과는 무조건 볼 수 있다.
    if stack:
        answer += 1

    stack.append((h, cnt))


print(answer)