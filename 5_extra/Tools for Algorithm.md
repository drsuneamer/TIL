## 2차원 배열 정렬

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

