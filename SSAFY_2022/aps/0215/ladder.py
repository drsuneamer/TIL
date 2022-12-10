T = 10
for tc in range(1, T+1):
    N = int(input())
    # 양쪽 끝에 0 추가
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 결과에서부터 올라가기
    j = 0
    for i in range(1, 101):
        if ladder[99][i] == 2:  # 도착점(2)를 만나면
            j = i              # 시작점의 열 값이 정해짐
            break
    # 방향 : 위, 왼쪽, 오른쪽
    di = (-1, 0, 0)
    dj = (0, -1, 1)

    # 위로 올라가기 시작 (99, j에서)
    i = 99
    k = 0

    while i > 0:
        if k == 0 and ladder[i][j-1] == 1:    # 위 -> 왼쪽
            k = 1
            i = i + di[k]
            j = j + dj[k]
        elif k == 0 and ladder[i][j+1] == 1:    # 위 -> 오른쪽
            k = 2
            i = i + di[k]
            j = j + dj[k]
        elif ladder[i + di[k]][j + dj[k]] == 0 and k in [1, 2]: # 왼쪽, 오른쪽 -> 위
            k = 0
            i = i + di[k]
            j = j + dj[k]
        elif ladder[i+di[k]][j+dj[k]] == 1:   # 가던 방향으로 계속
            i = i+di[k]
            j = j+dj[k]

    print(f'#{tc} {j - 1}')