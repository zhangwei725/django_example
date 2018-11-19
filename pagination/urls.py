from django.conf.urls import url

from pagination import views

urlpatterns = [
    url('list/', views.pg_list)
]
