# 2480. 주사위 세개  2022-03-03

a, b, c = map(int, input().split())
lst = [a, b, c]

if a == b == c:
    result = 10000 + a*1000
elif a == b and a != c:
    result = 1000 + a*100
elif a == c and a != b:
    result = 1000 + a*100
elif c == b and a != c:
    result = 1000 + c*100
elif a != b and b != c and a != c:
    result = max(lst) * 100

print(result)