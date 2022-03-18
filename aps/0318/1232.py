def in_order(v):
    global result
    if v:
        in_order(ch1[v])
        for i in range(N):
            if type(val[v]) == int:
                if ch1[i] == v:
                    if type(val[ch2[i]]) == int:
                        result += '('
        result += str(val[v])
        for i in range(N):
            if type(val[v]) == int:
                if ch2[i] == v:
                    if type(val[ch1[i]]) == int:
                        result += ')'
        in_order(ch2[v])


for tc in range(1, 11):
    N = int(input())
    val = [0] * (N+1)     # 각 노드에 저장된 값
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    result = ''
    for i in range(N):
        lst = list(input().split())
        if len(lst) == 2:
            val[i + 1] = int(lst[1])
        else:
            val[i+1] = lst[1]
        if len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])

    in_order(1)
    print(int(eval(result)))
