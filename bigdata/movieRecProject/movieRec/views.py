from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext

from .models import *
from .loadResult import load_result


def index(request):
    return render(request, 'movieRec/base.html', {})


def train_view(request):
    context = {}
    context['train_finished'] = False
    return render(request, 'movieRec/train.html', context)
    # context에 주어진 정보를 이용해서 train.html 파일을 이용해 화면에 보여줘라


n_recomm = 10
def recomm_main_view(request):
    global n_recomm
    n_recomm = request.POST.get('n_recomm')
    if n_recomm is None: n_recomm = 10
    user_list = User.objects.all()
    return render(request, 'movieRec/recomm.html', {'user_list':user_list, 'n_recomm':n_recomm})


def recomm_user(request, user_id):
    global n_recomm
    target_user = User.objects.get(id=user_id)
    viewed_list = Viewed.objects.filter(user=target_user).order_by('-rating')
    viewed_paginator = get_paginated_list(request, viewed_list)
    recomm_list = Recomm.objects.filter(user=target_user).order_by('-score')[:int(n_recomm)]
    return render(request, 'movieRec/recommResult.html', {'target_user':target_user, 'viewed_page':viewed_paginator, 'recomm_list':recomm_list})


def get_paginated_list(request, obj_list, page_size=10):
    paginator = Paginator(obj_list, page_size)
    page = request.GET.get('page')
    return paginator.get_page(page)


import os
def train_model(request):
    # request.POST 함수를 이용해 어떤 모델이 선택되었는지를 알아내 model 변수에 저장
    model = request.POST.get('model')
    if model == 'KNN': run_kNN(request)     # run_KNN 함수를 호출
    elif model == 'MF': run_MF(request)
    elif model == 'MF_PLSI': run_MF_PLSI(request)
    request.POST = {}
    return render(request, 'movieRec/train.html', {'train_finished':True, 'model':model})
    # render()를 movieRec/train.html 템플릿과 model 정보를 가지고 호출

def run_kNN(request):
    k = request.POST.get('param_k')
    # os.system: command line에서 돌아가는 것
    os.system('cd matrixfactorization& python train.py -i data/tiny -o result/tiny -a 0 -k %s'%k)
    # -i: 데이터 파일 디렉토리
    # -o: 결과 파일 디렉토리
    # -a: 0 (kNN 학습 알고리즘을 나타냄)
    load_result('matrixfactorization')
    # train 후 결과 저장
    # load_result 함수를 'matrixfactorization'를 입력으로 호출


def run_MF(request):
    os.system('cd matrixfactorization& python train.py -i data/tiny -o result/tiny -a 1')
    load_result('matrixfactorization')


def run_MF_PLSI(request):
    d = request.POST['param_nz']
    os.system('cd matrixfactorization& python train.py -i data/tiny -o result/tiny -a 2 -d %s'%d)
    load_result('matrixfactorization')

