from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import datetime

from django.shortcuts import render_to_response

from django.conf import settings

def index(request):
    return HttpResponse("Hello World")

def tody_is(request):
    now = datetime.datetime.now()
    # 年： new.year, 月：new.month 日： now.day
    # return render_to_response('blog/datetime.html', {'now': now})
    return render(request, 'blog/datetime.html', {'now': now, 'template_name': 'blog/nav.html', 'base_dir': settings.BASE_DIR })