from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext,render
from .models import Work

import time,datetime

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def publish(request):
	books = Work.objects.all()
	return render(request,'home.html',{'books':books})


