T = int(input())
for tc in range(1, T+1):
    code = list(map(str, input().split()))
    stack = []
    result = ''

    for i in range(len(code)):
        if code[i] in ['+', '-', '*', '/']:     # 연산자를 만나면(. 제외)
            if len(stack) >= 2:     # 숫자 2개 이상, 연산자 정상 작동
                if code[i] == '+':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a+b)
                if code[i] == '-':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a-b)
                if code[i] == '*':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a*b)
                if code[i] == '/':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a/b)
            else:
                result = 'error'    # 숫자 2개 이하, 에러
                break
        elif code[i] == '.':
            if len(stack) == 1:     # 결과만 남았을 때 .을 만날 경우
                result = int(stack.pop())  # 결과 출력
                break
            else:
                result = 'error'
                break
        else:       # 연산자 제외(정수)를 만나면
            stack.append(code[i])
    print(f'#{tc} {result}')