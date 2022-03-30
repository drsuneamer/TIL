# [D2] 5097. 회전  2022-03-22

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 0

    for i in range(M):
        # idx = (idx + 1) % N
        if idx >= N:
            idx = 0
        idx += 1

    print(f'#{tc} {arr[idx]}')