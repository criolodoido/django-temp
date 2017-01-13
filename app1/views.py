from django.shortcuts import render

def inicial(request):
	return render(request, 'principal/inicial.html')
# Create your views here.
