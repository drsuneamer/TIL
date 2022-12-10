def count_sort(N): # 0 이상 9 이하의 정수에 대한 정렬
    cnt = [0] * 10
    for i in range(N):  # 카운트 배열
        cnt[arr[i]] += 1

    for j in range(1, 10):
        cnt[j] += cnt[j-1]

    for i in range(N-1, -1, -1):
        cnt[arr[i]] -= 1
        tmp[cnt[arr[i]]] = arr[i]

N = int(input())
arr = list(map(int, input().split()))
tmp = [0] * N
count_sort(N)
print(tmp)
