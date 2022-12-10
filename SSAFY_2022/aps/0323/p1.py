arr = list(map(int, input()))
n = 6
dec = 0
for x in arr:
    dec += x * (2**n)
    n -= 1
    if n == -1:
        n = 6
        print(dec, end=" ")
        dec = 0
