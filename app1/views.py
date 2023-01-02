from django.shortcuts import render

def highest(request):

    d={'a':20, 'b':30}

    return render(request,'highest.html',d)
