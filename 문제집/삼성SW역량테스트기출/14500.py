# https://www.acmicpc.net/problem/14500
'''
테트로미노 5종류를 종이 위에 놓아 가린 부분의 점수의 합이 최대가 되는 수를 구하기
브루트 포스로 하는데 회전, 대칭이 다 된다.
'''

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

def long_one(i, j):
    ver, hor = 0, 0
    if i+3 < N:
        for k in range(4):
            ver += paper[i+k][j]
    if j+3 < M:
        for k in range(4):
            hor += paper[i][j+k]

    return max(ver, hor)

def square_one(i, j):
    if i + 1 < N and j + 1 < M:
        return paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]

    return -1

def f_one(i, j):
    a,b,c,d = 0,0,0,0
    if i+2<N:
        # ㅏ
        if j + 1 < M:
            a = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]
        # ㅓ
        if j > 0:
            b = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j-1]
    if j+2<M:
        # ㅜ
        if i+1<N:
            c = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]
        # ㅗ
        if i > 0:
            d = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i - 1][j + 1]

    return max(a,b,c,d)

def L_one(i, j):
    a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0

    if i + 2 < N and j + 1 < M:
        a = (paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j + 1])
        b = (paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i][j + 1])
        c = (paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1] + paper[i + 2][j])
        d = (paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1] + paper[i][j])

    if i + 1 < N and j + 2 < M:
        e = (paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j])
        f = (paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 2])
        g = (paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2] + paper[i][j])
        h = (paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2] + paper[i][j + 2])

    return max(a,b,c,d,e,f,g,h)

def s_one(i, j):
    a,b,c,d = 0,0,0,0

    if i + 2 < N and j + 1 < M:
        a = (paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1])
        b = (paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j] + paper[i + 2][j])
    if i + 1 < N and j + 2 < M:
        c = (paper[i + 1][j] + paper[i + 1][j + 1] + paper[i][j + 1] + paper[i][j + 2])
        d = (paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j + 2])

    return max(a,b,c,d)

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(long_one(i,j), square_one(i,j), f_one(i,j), L_one(i,j), s_one(i, j), answer)

print(answer)