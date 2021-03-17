from django.shortcuts import render

# Create your views here.
def r1(request):
    return render(request,'h1.html')
def r2(request):
    return render(request,'h2.html')
