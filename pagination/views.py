from django.shortcuts import render

from pagination.models import Film


def pg_list(request):
    films = Film.objects.all()
    return render(request, 'pagination_demo.html', locals())
