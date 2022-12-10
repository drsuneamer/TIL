h2b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
       '1000', '1001', '1010', '1011' '1100', '1101', '1110', '1111' ]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    for i in range(N):
        if '0' <= arr[i] <= '9':
            arr[i] = int(arr[i])
        else:   #'A' ~ 'F'
            arr[i] = ord(arr[i]) - ord('A') + 10
    s = ''
    for i in range(N):
        s += h2b[arr[i]]
    print(s)
