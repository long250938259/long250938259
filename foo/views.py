from django.shortcuts import render
import datetime
from django.http import HttpResponse


def sayHello(request):
    s = '技术的高房价但是广泛接受的但是看见浩方空间的!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


# Create your views here.
