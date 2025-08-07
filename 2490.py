# https://www.acmicpc.net/problem/2490

for _ in range(3):
    yut = list(map(int, input().split()))
    bae = yut.count(0)

    if bae == 0:
        print('E')
    elif bae == 1:
        print('A')
    elif bae == 2:
        print('B')
    elif bae == 3:
        print('C')
    elif bae == 4:
        print('D')
