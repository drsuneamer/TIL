def bus(start, end, left, cnt):
    global ans
    if start == end:
        if cnt < ans:   # 도착하면 최소값과 비교
            ans = cnt

    elif cnt > ans:     # 최소값 이미 넘어서면 리턴
        return

    else:
        if left > 0:    # 남아있으면 통과 / 교체 중 선택
            bus(start + 1, end, left - 1, cnt)  # 통과
            bus(start + 1, end, lst[start] - 1, cnt + 1)   # 교체
        else:   # 남아있지 않으면 무조건 교체
            bus(start + 1, end, lst[start] - 1, cnt + 1)  # 교체


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    ans = N

    # 목적지에 도착하는 데 필요한 최소한의 교환 횟수
    bus(1, N - 1, lst[0] - 1, 0)
    print(f'#{tc} {ans}')