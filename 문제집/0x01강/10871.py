A, X = map(int, input().split())
nums = list(map(int, input().split()))

print(*[i for i in nums if i < X])