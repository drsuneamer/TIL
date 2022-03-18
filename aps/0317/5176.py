def in_order(v):
    global cnt
    if v <= N:
        in_order(v * 2)
        cnt += 1
        tree[v] = cnt
        in_order(v * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 방문 횟수
    cnt = 0
    # 각 노드에 해당하는 값 저장할 리스트
    tree = [0] * (N + 1)
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')