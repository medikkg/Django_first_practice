from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'website/index.html', context)


def about(request):
    context = {
        'title': 'О компании',
    }
    return render(request, 'website/about.html', context)


def blog(request):
    context = {
        'title': 'Блог директора',
    }
    return render(request, 'website/blog.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'website/contact.html', context)


def service(request):
    return render(request, 'website/service.html')
