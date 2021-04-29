"""django_explore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foo.views import sayHello
from foo.views import regist, login, logout, index, share
from django.conf.urls import  include, url
# from foo.views import regist

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'sayhello/', sayHello),
    url(r'^login/$', login, name="login"),
    # path(r'regist/', UserForm),
    url(r'^index/$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^share/$', share, name="share"),
    url(r'^regist/$', regist, name="regist"),

]


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'form_test.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     path(r'^admin/', include(admin.site.paths)),
#     path(r'^$', 'foo.views.login',name='login'),
#     path(r'^login/$', 'foo.views.login',name='login'),
#     path(r'^regist/$', 'foo.views.regist',name='regist'),
#     path(r'^index/$', 'foo.views.index',name='index'),
#     path(r'^logout/$', 'foo.views.logout',name='logout'),
#     path(r'^share/$', 'foo.views.share',name='share'),
# )
