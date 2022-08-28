# 02_KNN_추천

> [강의영상](https://edu.ssafy.com/edu/board/free/detail.do?brdItmSeq=47342&listMenu=&_csrf=cb98bb55-e4c1-4df0-8519-b698e63cf574) 

![image-20220826011234643](02_KNN_추천.assets/image-20220826011234643.png)



## MovieRecProject/matrixFactorization 디렉토리

![image-20220826011242959](02_KNN_추천.assets/image-20220826011242959.png)



![image-20220825022224710](02_KNN_추천.assets/image-20220825022224710.png)

![image-20220825022436285](02_KNN_추천.assets/image-20220825022436285.png)

![image-20220825024509066](02_KNN_추천.assets/image-20220825024509066.png)

![image-20220825024740177](02_KNN_추천.assets/image-20220825024740177.png)

![image-20220825024900626](02_KNN_추천.assets/image-20220825024900626.png)

![image-20220825025046473](02_KNN_추천.assets/image-20220825025046473.png)

![image-20220825165358834](02_KNN_추천.assets/image-20220825165358834.png)

![image-20220825165459725](02_KNN_추천.assets/image-20220825165459725.png)

![image-20220826021005273](02_KNN_추천.assets/image-20220826021005273.png)



## Recommend 함수 코딩

![image-20220826021051860](02_KNN_추천.assets/image-20220826021051860.png)

![image-20220826021102978](02_KNN_추천.assets/image-20220826021102978.png)

![image-20220826021957661](02_KNN_추천.assets/image-20220826021957661.png)

![image-20220826022107188](02_KNN_추천.assets/image-20220826022107188.png)

![image-20220826022326143](02_KNN_추천.assets/image-20220826022326143.png)

![image-20220826024304931](02_KNN_추천.assets/image-20220826024304931.png)

![image-20220826024446193](02_KNN_추천.assets/image-20220826024446193.png)



## Recommend 함수 코딩 시작

![image-20220826024459640](02_KNN_추천.assets/image-20220826024459640.png)



## KNN 추천 시스템

![image-20220826024538785](02_KNN_추천.assets/image-20220826024538785.png)

![image-20220826024529389](02_KNN_추천.assets/image-20220826024529389.png)

![image-20220826024634554](02_KNN_추천.assets/image-20220826024634554.png)



## 기본 KNN 코딩

![image-20220826024806657](02_KNN_추천.assets/image-20220826024806657.png)

![image-20220826024817019](02_KNN_추천.assets/image-20220826024817019.png)

![image-20220826025028532](02_KNN_추천.assets/image-20220826025028532.png)

![image-20220826025152196](02_KNN_추천.assets/image-20220826025152196.png)

![image-20220826025222489](02_KNN_추천.assets/image-20220826025222489.png)

![image-20220826025338209](02_KNN_추천.assets/image-20220826025338209.png)

![image-20220826173656761](02_KNN_추천.assets/image-20220826173656761.png)

![image-20220826174028430](02_KNN_추천.assets/image-20220826174028430.png)

![image-20220826174235180](02_KNN_추천.assets/image-20220826174235180.png)

![image-20220826174244588](02_KNN_추천.assets/image-20220826174244588.png)

![image-20220826174249388](02_KNN_추천.assets/image-20220826174249388.png)

![image-20220826174329229](02_KNN_추천.assets/image-20220826174329229.png)



# 📑 과제 해설

![image-20220826174417627](02_KNN_추천.assets/image-20220826174417627.png)



## Recommend 함수

![image-20220826174428099](02_KNN_추천.assets/image-20220826174428099.png)

![image-20220826174434511](02_KNN_추천.assets/image-20220826174434511.png)

```python
def recommend(R_train, R_predicted, item_ids, output_path):
    # write train ratings
    # 해당 디렉토리(output_path)의 train_ratings 사용
    with open(output_path + '/train_ratings.txt', 'w') as f:
        rows, cols = R_train.nonzero()
        # nonzero에 해당하는 좌표들
        for row, col in zip(rows, cols):
            f.write('%d::%s::%.1f\n' % (row, item_ids[col], R_train[row, col]))
            # remove train data from recommendation
            # 자기 자신이 본 영화는 추천하지 않음 (0으로 만들어서)
            R_predicted[row, col] = 0

    # write recommend ratings
    with open(output_path + '/recommend_ratings.txt', 'w') as f:
        # 모든 possible한 행렬 좌표 loop
        for i in range(R_predicted.shape[0]):   # 행의 개수
            for j in range(R_predicted.shape[1]):   # 열의 개수
                if R_predicted[i, j] > 1:   # 1보다 크면 사용
                    f.write('%d::%s::%.3f\n' % (i, item_ids[j], R_predicted[i, j]))

```



## compute_sim_inner 함수

![image-20220826174601924](02_KNN_추천.assets/image-20220826174601924.png)

![image-20220826174646922](02_KNN_추천.assets/image-20220826174646922.png)

```python
def compute_sim(R):
    num_users = R.shape[0]
    # dense matrix 위해 toarray 사용
    UbyU = (R * R.transpose()).toarray()
    # 자신과의 유사도 0으로 만듦
    UbyU[range(num_users), range(num_users)] = 0
    # 결과 array return
    return UbyU
```



## Predict 함수

![image-20220826174715926](02_KNN_추천.assets/image-20220826174715926.png)

![image-20220826174722208](02_KNN_추천.assets/image-20220826174722208.png)

![image-20220826174755391](02_KNN_추천.assets/image-20220826174755391.png)