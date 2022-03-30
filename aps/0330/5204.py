# Merge Sort

def merge_sort(l):
    if len(l) <= 1:
        return l

    left = []
    right = []
    m = len(l) // 2
    for i in range(m):
        left.append(l[i])
    for j in range(m, len(l)):
        right.append(l[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(L, R):
    global cnt
    result = []
    i = j = 0
    if L[-1] > R[-1]:
        cnt += 1

    while i < len(L) or j < len(R):
        if i < len(L) and j < len(R):
            if L[i] < R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        elif i < len(L):
            result.append(L[i])
            i += 1
        elif j < len(R):
            result.append(R[j])
            j += 1
    return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(lst)[N//2]} {cnt}')

