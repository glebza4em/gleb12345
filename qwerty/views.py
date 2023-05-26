from django.http import HttpResponse


def first(request):
    return HttpResponse("<h1>Hello World</h1>")

def second_func(request):
    return HttpResponse("<h1>Gleb</h1>")

def third_func(requests):
    return HttpResponse("<h1>19 years</h1>")