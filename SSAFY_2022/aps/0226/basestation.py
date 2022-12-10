T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # 오른쪽 - 아래 - 왼쪽 - 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0

    for i in range(n):  # nxn 배열
        for j in range(n):
            now = arr[i][j]
            if now in ['A', 'B', 'C']:
                if now == 'A':
                    cover = 1
                elif now == 'B':
                    cover = 2
                elif now == 'C':
                    cover = 3
                for k in range(4):
                    for l in range(1, cover+1): # 기지국 종류마다 다른 cover의 범위만큼
                        ii = i + (di[k] * l)
                        jj = j + (dj[k] * l)
                        if 0 <= ii < n and 0 <= jj < n:
                            if arr[ii][jj] == 'H':  # 집을 만나면 X로 변경
                                arr[ii][jj] = 'X'

    # 지워지지 않은 H의 수 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                ans += 1

    print(f'#{tc} {ans}')

