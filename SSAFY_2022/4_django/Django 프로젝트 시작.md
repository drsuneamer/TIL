## Django 프로젝트 시작



### 가상환경 생성

```bash
$ python -m venv venv
# venv 폴더가 생긴다
```



### 가상환경 시작

```bash
$ source venv/Scripts/activate
(venv)
# activate를 실행시킨다
```



### git 사용시

```python
# .gitignore

venv/
__pycache__/
```

<img src="Django 프로젝트 시작.assets/image-20220308100940143.png" alt="image-20220308100940143" style="zoom:150%;" />



### 장고 설치

```bash
$ pip install django==3.2.12
```



### 프로젝트 생성

```bash
$ django-admin startproject [프로젝트이름] .
(venv) 
```



### 앱 생성

```bash
$ python manage.py startapp articles
(venv) 
```



### 앱 등록

```python
# pjt > settings.py

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



### 날짜 및 시간

```python
LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'
```





### URL

```python
# pjt > urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'articles.urls' => articles 앱의 urls.py
    path('articles/', include('articles.urls')),
]
```

```python
# articles > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello)
]
```





### 템플릿 상속

- 프로젝트, 앱과 같은 위치에 [templates] 폴더 생성
- 그 안에 `'base.html'` 생성
- HTML 기본 구조(!tab) 이후 body 안에
- 부트스트랩 사용 시 - css는 head 안에, js는 body 가장 밑에

```django
<div class="container">
	{% block content %}
    {% endblock %}
</div>
```

```django
<!-- 혹은 그냥 이렇게.. -->
{% block content %}
{% endblock %}
```



- 앱 안에 생성시킨 templates 폴더 안의 html  파일에는

```django
{% extends 'base.html' %}

{% block content %}
  
{% endblock %}
```

- templates 폴더 경로 추가

```python
# pjt > settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```





### view

```python
# articles > views.py

from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello.html')
```











