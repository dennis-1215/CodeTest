s = input().strip()

stack = []
answer = 0

tmp = 1

for i, c in enumerate(s):
    if c == '(':
        stack.append(c)
        tmp *= 2

    elif c == '[':
        stack.append(c)
        tmp *= 3

    elif c == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if s[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp//=2

    elif c == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if s[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp//=3

if stack:
    answer = 0

print(answer)