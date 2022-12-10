T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    max_cnt = 0
    cnt = 0

    for i in range(N):
        if nums[i] == 0:
            cnt = 0
        elif nums[i] == 1:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt

    print(max_cnt)
