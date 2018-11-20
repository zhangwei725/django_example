from django.conf.urls import url

from apps.reverse_ex import views

urlpatterns = [
    url('index/', views.reverse_index),
    url(r'base/', views.reverse_base, name='base'),
    url(r'space/', views.reverse_ns, name='space'),
    # 动态路由
    url(r'params/(\d+)/(\d+)/', views.reverse_index, name='params'),
    url(r'kw/(?P<id>\d+)/', views.reverse_kw, name='kw'),
    url(r'rm/', views.redirect_reverse),
]
