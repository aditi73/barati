from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard

#@login_required(login_url='/auth/login/')
def Contact_Us(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/contact_us.html', context_dict, context_instance=context)
