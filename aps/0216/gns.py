T = int(input())
for tc in range(1, T+1):
    N, L = input().split()
    L = int(L)
    arr = list(input().split())
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_arr = [0] * L

    # 숫자로 변경한 list 만들기
    for i in range(L):
        for j in range(10):
            if arr[i] == new_nums[j]:
                new_arr[i] = j

    # 정렬
    for i in range(L-1, 0, -1):
        for j in range(i):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]

    result = [0] * L

    # 다시 문자열로 출력
    for i in range(L):
        for j in range(10):
            if new_arr[i] == nums[j]:
                result[i] = new_nums[j]

    print(f'#{tc}')
    for i in result:
        print(i, end=' ')
    print()