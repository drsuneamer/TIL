def in_order(v):
    global ans
    if v:
        in_order(ch1[v])
        ans += words[v-1]
        in_order(ch2[v])

for tc in range(1, 11):
    N = int(input())
    V = N + 1
    words = []
    ch1 = [0] * V
    ch2 = [0] * V
    ans = ''
    for i in range(N):
        lst = list(input().split())
        words.append(lst[1])
        if len(lst) > 2:
            ch1[int(lst[0])] = int(lst[2])
        if len(lst) > 3:
            ch2[int(lst[0])] = int(lst[3])

    in_order(1)
    print(f'#{tc} {ans}')