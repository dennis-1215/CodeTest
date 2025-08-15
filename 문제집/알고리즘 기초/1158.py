# https://www.acmicpc.net/problem/1158
'''
요세푸스 문제로 원형으로 앉아 있는 사람들을 K번째 사람을 제거하는 문제이다.
이는 큐를 이용하면 쉽게 구현 가능하다.
'''

from collections import deque
N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])
answer = '<'

while len(q) > 1:
    q.rotate(-(K-1))
    num = q.popleft()
    answer += str(num)+', '

answer += str(q.pop())+'>'
print(answer)