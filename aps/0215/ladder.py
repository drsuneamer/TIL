T = 10
for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 결과에서부터 올라가기
    j = 0
    for i in range(100):
        if ladder[99][i] == 2:  # 도착점(2)를 만나면
            j = i              # 시작점의 열 값이 정해짐
            break
    # 방향 : 위, 왼쪽, 오른쪽
    di = (-1, 0, 0)
    dj = (0, -1, 1)

    # 위로 올라가기 시작 (99, dj에서)
    i = 99
    k = 0
    while i != 0:
        if ladder[i][j-1] == 0 and ladder[i][j+1] == 0:
            i += di[k]
            j += dj[k]
        elif ladder[i][j-1] != 0:
            i -= di[k]
            j -= dj[k]
            k = 1
            i, j = i + di[k], j + dj[k]
        elif ladder[i][j+1] != 0:
            i -= di[k]
            j -= dj[k]
            k = 2
            i, j = i + di[k], j + dj[k]




    print(dj)