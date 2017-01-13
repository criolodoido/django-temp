from django.shortcuts import render


def primeiro(request):
    return render(request, 'app2/primeiro.html')
