import sys
sys.stdin = open("input.txt")


def quick_sort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick_sort(arr, l, s - 1)
        quick_sort(arr, s + 1, r)


def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


lst = list(map(int, input().split()))
N = len(lst)

quick_sort(lst, 0, N-1)
print(lst[500000])