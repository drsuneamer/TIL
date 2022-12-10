T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_n = nums[0]
    min_n = nums[0]

    for n in nums:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n

    print(f'#{tc} {max_n - min_n}')


