import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import views

logger = logging.getLogger(__name__)


def reverse_index(request):
    return render(request, 'reverse.html')


def reverse_base(request):
    return render(request, 'base.html')


def reverse_ns(request):
    return render(request, 'reverse_ns.html')


def reverse_params(request, page, size):
    return render(request, 'reverse_params.html')


def reverse_kw(request, id):
    return HttpResponse(id)


def redirect_reverse(request):
    # 通过路由中的别名(索引名)
    base = reverse('index')  # /index/
    # 通过视图函数名
    path_base = reverse(views.pg_list)  #
    patt_params = reverse('reverse:params', args=[1, 10])
    path_kw = reverse('reverse:kw', kwargs={'id': 1})
    return redirect(base)
