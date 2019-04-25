from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')

def add(request):
    try:
        i=request.GET['t1']
        j=request.GET['t2']
        x=int(i)
        y=int(j)
        z=x+y
        return HttpResponse("<html> <body bgcolor=gray> <h1>sum is: "+str(z)+" </h1></body></html>")
    except(ValueError):
        return HttpResponse("invalid input")

