def win1(lst):
    for i in range(len(lst)):
        if lst[i] >= 3:
            return 1
    for i in range(len(lst)-2):
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            return 1
    return 0


def win2(lst):
    for i in range(len(lst)):
        if lst[i] >= 3:
            return 2
    for i in range(len(lst)-2):
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:
            return 2
    return 0


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0

    for i in range(12):
        if ans != 0: break
        if i % 2 != 1:
            p1[lst[i]] += 1
            ans = win1(p1)
        else:
            p2[lst[i]] += 1
            ans = win2(p2)

    print(ans)