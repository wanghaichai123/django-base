from django.shortcuts import render

# Create your views here.
'''
所谓的视图其实就是python函数，视图函数有2个要求：
1、视图函数的第一个参数就是接收请求，这个请求其实就是HttpRequest的类对象
2、必须返回一个响应
'''
from django.http import HttpRequest
from django.http import HttpResponse
'''
希望用户输入这个地址http://127.0.0.1:8000/index/来访问视图函数
'''
def index(request):
    context = {'name':'2022年的双11，你买了什么呢？'}
    return render(request,'book/index.html',context=context)
    # return HttpResponse('ok')
