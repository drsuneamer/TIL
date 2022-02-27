T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()     # 후위 표기 변환 전
    postfix = ''
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선 순위 (문제 조건: *, +만 등장)

    for i in range(N):
        if '0' <= infix[i] <= '9':  # 문제 조건: 0부터 9 사이 정수
            postfix += infix[i]     # 정수는 문자열에 바로 저장
        else:   # 연산자일 때
            # stack 가장 맨 위의 연산자보다 우선순위가 높으면
            while top > -1 and icp[stack[top]] >= icp[infix[i]]:
                # stack 안에 있는 연산자 문자열에 저장
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]   # 그렇지 않을 경우 문자열에 저장

    while top > -1:    # stack 안에 남은 요소 다시 문자열에
        postfix += stack[top]
        top -= 1

    st2 = []
    for i in postfix:
        # 연산자일 경우
        if i == '+':
            b = int(st2.pop())
            a = int(st2.pop())
            st2.append(a + b)
        elif i == '*':
            b = int(st2.pop())
            a = int(st2.pop())
            st2.append(a * b)
        # 피연산자일 경우
        else:
            st2.append(i)

    print(f'#{tc}', st2[0])
