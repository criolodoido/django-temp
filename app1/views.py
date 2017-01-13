from django.shortcuts import render


def inicial(request):
    return render(request, 'app1/inicial.html')
