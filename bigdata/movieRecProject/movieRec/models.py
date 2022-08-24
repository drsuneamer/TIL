from django.db import models


# 고객에 대한 정보 저장
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

# 영화에 대한 정보 저장
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=False)
    img = models.ImageField(blank=True, null=True)
    text = models.CharField(max_length=1000)

# 고객이 시청한 영화들에 대한 정보 저장
class Viewed(models.Model):
    # User 테이블의 기본 키인 id 속성에 대한 외래키
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()

# 고객에게 시청하지 않은 영화들에 대해서 예상 평점을 저장
class Recomm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.FloatField() # 보지 않은 영화들에 예상 평점 저장
