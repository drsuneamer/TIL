T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    l, r = 1, P
    cnt_a = 0   # A 실행 횟수 찾기
    while l < r:
        c = int((l+r)//2)
        if Pa == c:
            break
        elif Pa > c:
            l = c
            cnt_a += 1
        elif Pa < c:
            r = c
            cnt_a += 1

    l, r = 1, P
    cnt_b = 0   # B 실행 횟수 찾기
    while l < r:
        c = int((l+r)//2)
        if Pb == c:
            break
        elif Pb > c:
            l = c
            cnt_b += 1
        elif Pb < c:
            r = c
            cnt_b += 1

    if cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a > cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
