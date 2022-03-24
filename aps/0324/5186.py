T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    i = 1

    while 1:
        if N == 0:
            print(f'#{tc} {ans}')
            break
        if len(ans) >= 13:
            print(f'#{tc} overflow')
            break
        if N >= (2 ** -i):
            ans += '1'
            N -= (2 ** -i)
        else:
            ans += '0'
        i += 1