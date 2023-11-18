from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20}
    return render(request,'condition.html',d)

def ifelse(request):
    d={'a':20,'b':5}
    return render(request,'ifelse.html',d)

def ifelifelse(request):
    d={'a':20,'b':5,'c':56}
    return render(request,'ifelifelse.html',d)

def nestedif(request):
    d={'a':20,'b':5,'c':56}
    return render(request,'nestedif.html',d)
