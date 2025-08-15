# https://www.acmicpc.net/problem/4883

import sys
input = sys.stdin.readline

t = 0
while True:
    t += 1
    N = int(input())

    if N == 0:
        exit()

    graph = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')

    DP = [[INF]*3 for _ in range(N)]
    DP[0] = graph[0]
    DP[0][2] = DP[0][1]+graph[0][2]

    DP[1][0] = DP[0][1] + graph[1][0]
    DP[1][1] = min(DP[0][1] + graph[1][1], DP[0][2] + graph[1][1], DP[1][0] + graph[1][1])
    DP[1][2] = min(DP[0][1] + graph[1][2], DP[0][2] + graph[1][2], DP[1][1] + graph[1][2])

    for i in range(2, N):
        DP[i][0] = min(DP[i-1][0] + graph[i][0], DP[i-1][1] + graph[i][0])
        DP[i][1] = min(DP[i-1][0] + graph[i][1],
                       DP[i-1][1] + graph[i][1],
                       DP[i-1][2] + graph[i][1],
                       DP[i][0] + graph[i][1]
                       )
        DP[i][2] = min(DP[i-1][1] + graph[i][2],
                       DP[i-1][2] + graph[i][2],
                       DP[i][1] + graph[i][2]
                       )


    print(f"{t}. {DP[N-1][1]}")

'''
4
13 7 -900
7 13 6
14 3 12
15 6 16
0
'''