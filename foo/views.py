from django.shortcuts import render
#coding:utf-8
from django.shortcuts import render, render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from foo.models import User
import datetime
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt





class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            #User.objects.get_or_create(username = username,password = password)
            registAdd = User.objects.get_or_create(username = username, password = password)[1]
            print(registAdd)
            if registAdd == False:
                #return HttpResponseRedirect('/share/')
                req1 = {}
                req1["username"] = username
                return render(req,'share.html',context=req1)
            else:
                return render(req ,'share.html')

    else:
        uf = UserForm()
    return render(req ,'regist.html', {'uf': uf})

# def regist(request):
#     return render(request, "regist.html")


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #对比提交的数据与数据库中的数据
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                #将username写入浏览器cookie，失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(req ,'login.html', {'uf': uf})
#登录成功
def index(req):
    username = req.COOKIES.get('username','')
    return render(req, 'index.html',{'username':username})
#退出登录

def logout(req):
    response = HttpResponse('logout!!!')
    #清除cookie里保存的username
    response.delete_cookie('username')
    return response

def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render(req ,'share.html',{'username':username})
    else:
        uf = UserForm()
    return render(req , 'share.html',{'uf':uf})


def sayHello(request):
    s = '技术的高房价但是广泛接受的但是看见浩方空间的!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


# def regist(request):
#     return render(request, "regist.html")



