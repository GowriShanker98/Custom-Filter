from django.shortcuts import render

# Create your views here.
def filter_demo(request):
    return render(request,"filter_demo.html",{'data':"hello world",'a':10,'b':20,'num':1})
    