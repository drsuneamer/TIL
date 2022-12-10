T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = ''
    stack = [0] * N
    top = -1
    # 연산자 : 괄호, +, *
    icp = {'(':3, '+':1, '*':2}
    isp = {'(':0, '+':1, '*':2}

    # 후위 문자열로 변경
    for i in infix:
        # 숫자인 경우
        if '0' <= i <= '9':
            postfix += i
        # 연산자인 경우
        else:
            if i == ')':
                while stack[top] != '(':
                    postfix += str(stack[top])
                    top -= 1
                if stack[top] == '(':
                    top -= 1
            else:
                while top > -1 and icp[stack[top]] >= icp[i]:
                    postfix += str(stack[top])
                    top -= 1
            top += 1
            stack[top] = i

    print(postfix)