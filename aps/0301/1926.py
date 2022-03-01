N = int(input())
for i in range(1, N+1):
    p = ''
    for j in str(i):
        if j in ['3', '6', '9']:
            p += '-'
        else:
            pass

    if p == '':
        print(i, end=" ")
    else:
        print(p, end=" ")
