from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)
