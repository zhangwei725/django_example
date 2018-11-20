from django.conf.urls import url

from apps.pagination import views

urlpatterns = [
    url('list/', views.pg_list)
]
