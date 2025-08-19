A = input()
B = input()
C = input()

num = str(int(A) * int(B) * int(C))
for i in range(10):
    print(num.count(str(i)))