T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W

    if W <= R:
        B = Q
    else:
        B = (W - R) * S + Q

    if A > B:
        print(f'#{tc} {B}')
    else:
        print(f'#{tc} {A}')