from django.http import HttpResponse
from django.shortcuts import render
import json

def hello(request):
    return HttpResponse("Hello World")

def mao(request):
    return HttpResponse("I am PeterMao")

def runoob(request):
    x = 1
    context  = {}
    context["hello"]  = x
    return render(request,"runoob.html",context)
def mao(request):
    views_name = "毛少雄"
    return render(request,"mao.html",{"var1" : views_name})
def mao1(request):
    arrays = ["Apple","Google","Amazon"]
    return render(request,"mao.html",{"array":arrays})
def mao2(request):
    var2 = {"name":"Maoshaoxiong"}
    return render(request,"mao.html",{"var2":var2})

def demo(request):
    dict_view = getvalue()
    return render(request,"demo.html",{"dict_view":dict_view})

def getvalue():
    file = open('/Users/neo/Coding/Python/django_test/demo_1/HelloWorld/HelloWorld/brushing_time.txt','r')
    js = file.read()
    dic = json.loads(js)
    file.close()
    return dic