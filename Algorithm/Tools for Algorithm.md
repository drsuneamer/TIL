### 2차원 배열 정렬

> https://asxpyn.tistory.com/75

```python
arr = [[2, 3], [1, 2], [0, 4]]
# 두번째 값 기준으로 오름차순 정렬
arr.sort(key = lambda x:x[1])
arr = [[1, 2], [2, 3], [0, 4]]
```



### 소수점 이하 자릿수 맞추기

>https://outofgreed.tistory.com/312

```python
score = '{:.2f}'.format(round(x,2))
# 8.50 (두번째 자리 채워짐)
```



### 에라토스테네스의 체

> https://wikidocs.net/21638

1. 1은 제거
2. 지워지지 않은 수 중 가장 작은 수인 2를 소수로 채택하고, 2의 배수를 모두 지운다
3. 지워지지 않은 수 중 가장 작은 수인 3을 소수로 채택하고, 3의 배수를 모두 지운다.
4. 지워지지 않은 수 중 가장 작은 수인 5를 소수로 ...

```python
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [1] * (n + 1)

    m = int(n ** 0.5)  # n의 최대 약수는 sqrt(n) 이하
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = 0

    return [x for x in range(2, n + 1) if sieve[x] == 1]
```

