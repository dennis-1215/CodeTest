A = list(map(str, input().strip()))
B = list(map(str, input().strip()))

diff = 0
for i in range(26):
    diff += abs(A.count(chr(97+i)) - B.count(chr(97+i)))

print(diff)
