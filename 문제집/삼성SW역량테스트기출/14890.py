# https://www.acmicpc.net/problem/14890
'''
N과 L이 주어지는데 L은 경사로의 길이고 경사로의 높이는 항상 1이다.
길은 열과 행을 말하는데 경사로를 깔아서 지나갈 수 있거나 높이가 모두 같아서 지나갈 수 있는
길의 개수를 구하는 문제다.

'''

N, L = map(int, input().split())
loads = [list(map(int, input().split())) for _ in range(N)]

def can_pass_road(road):
    used = [False] * N  # 경사로 설치 여부
    for i in range(N - 1):
        if road[i] == road[i + 1]:
            continue
        elif road[i] + 1 == road[i + 1]:  # 오르막
            for j in range(i, i - L, -1):
                if j < 0 or road[j] != road[i] or used[j]:
                    return False
                used[j] = True
        elif road[i] - 1 == road[i + 1]:  # 내리막
            for j in range(i + 1, i + L + 1):
                if j >= N or road[j] != road[i + 1] or used[j]:
                    return False
                used[j] = True
        else:
            return False
    return True

answer = 0
for i in range(N):
    row = loads[i]
    col = [loads[j][i] for j in range(N)]
    if can_pass_road(row):
        answer += 1
    if can_pass_road(col):
        answer += 1

print(answer)