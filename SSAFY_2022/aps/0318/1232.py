# [D4] 1232. 사칙연산  2022-03-19

def f(v):
    global result
    op = ['+', '-', '/', '*']
    if v:
        f(ch1[v])
        f(ch2[v])
        if val[v] in op:
            if val[v] == '+':
                result[v] = result[ch1[v]] + result[ch2[v]]
            if val[v] == '-':
                result[v] = result[ch1[v]] - result[ch2[v]]
            if val[v] == '*':
                result[v] = result[ch1[v]] * result[ch2[v]]
            if val[v] == '/':
                result[v] = result[ch1[v]] / result[ch2[v]]
        else:
            result[v] = val[v]



for tc in range(1, 11):
    N = int(input())
    val = [0] * (N+1)     # 각 노드에 저장된 값
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    result = [0] * (N+1)    # 계산 결과 저장할 값
    for i in range(N):
        lst = list(input().split())
        if len(lst) == 2:
            val[i + 1] = int(lst[1])
        else:
            val[i+1] = lst[1]
        if len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])

    f(1)
    print(f'#{tc} {int(result[1])}')