from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    now = datetime.datetime.now()
    response = "<html><body>The time is {0}</body></html>".format(now)
    return HttpResponse(response)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # t = get_template('time.html')
    # html = t.render(Context({'offset':offset, 'time':dt}))
    # return HttpResponse(html)
    return render(request, 'time.html', {'offset':offset, 'time':dt})