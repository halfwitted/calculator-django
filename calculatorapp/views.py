from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def submitquery(request):
    q = request.POST['query']
    try:
        ans = eval(q)
        calcdict = {
            "q" : q,
            "ans" : ans,
            "Error":False,
            "result":True
        }
        return render(request,'index.html',context=calcdict)
    except:
        calcdict = {
            "Error":True,
            "result":False
        }
        return render(request,'index.html',context=calcdict)
        
    