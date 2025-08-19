N = int(input())
call_time = list(map(int, input().split()))

Y, M = 0, 0
for time in call_time:
    Y += ((time//30)+1)*10
    M += ((time//60)+1)*15

if Y < M:
    print(f"Y {Y}")

elif Y == M:
    print(f"Y M {M}")

else:
    print(f"M {M}")