# 4866. 괄호검사  2022-02-22

T = int(input())
for tc in range(1, T+1):
    a = input()
    result = 1

    stack = [''] * len(a)
    top = -1

    for i in range(len(a)):
        if a[i] in ['{', '(']:      # 여는 괄호일 경우 stack에 삽입
            top += 1
            stack[top] = a[i]
        if a[i] == '}':             # 닫는 괄호일 경우 stack의 맨 위에 있는 여는 괄호와 맞는지 확인
            if stack[top] == '{':
                top -= 1
            else:
                result = 0
                break
        if a[i] == ')':
            if stack[top] == '(':
                top -= 1
            else:
                result = 0
                break

    if top != -1:   # stack 안에 남아 있는 경우
        result = 0

    print(f'#{tc}', result)