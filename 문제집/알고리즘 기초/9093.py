# https://www.acmicpc.net/problem/9093
'''
단어 뒤집기
I am happy today 을
I ma yppah yadot 로 바꿔 출력하면 된다.
'''

T = int(input())

for _ in range(T):
    strings = list(map(str, input().split()))

    for s in strings:
        for i in range(1, len(s)+1):
            print(s[-i], end='')
        print(' ', end='')