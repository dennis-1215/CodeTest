N = int(input())
for i in range(N):
    print(' '*i + '*'*(2*N-1-(i*2)))

for i in range(N-2, -1, -1):
    print(' ' * i + '*' * (2 * N - 1 - (i * 2)))
