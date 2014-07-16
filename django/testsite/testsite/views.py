from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world!")

def time(request):
    now = datetime.datetime.now()
    return render(request, 'time.html', {'time':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # t = get_template('future_time.html')
    # html = t.render(Context({'offset':offset, 'time':dt}))
    # return HttpResponse(html)
    return render(request, 'future_time.html', {'hours':offset, 'time':dt})