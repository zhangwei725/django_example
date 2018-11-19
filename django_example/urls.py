from django.contrib import admin
from django.conf.urls import url, include

from reverse_ex import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.reverse_index,name='index'),
    url('reverse/', include('reverse_ex.urls', namespace='reverse')),
    url('pagination/', include('pagination.urls')),
]
