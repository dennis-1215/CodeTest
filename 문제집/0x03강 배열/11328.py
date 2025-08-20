N = int(input())

for _ in range(N):
    A, B = map(str, input().split())

    if sorted(A) == sorted(B):
        print("Possible")
    else:
        print("Impossible")