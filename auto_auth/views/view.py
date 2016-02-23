#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from auto_auth.views.permission import SupperVerify
# Create your views here.
@login_required
@SupperVerify()
def Home(request):
   return render_to_response('auto_auth/home.html',locals(),RequestContext(request))
