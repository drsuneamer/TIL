T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    nums = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                sti, stj = i, j
                break

    C = ''.join(arr[sti][stj-55:stj+1])
    code = []

    for i in range(0, 56, 7):
        c = C[i:i+7]
        for j in nums:
            if j == c:
                code.append(nums.index(j))

    check = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]

    if check % 10 != 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(code)}')