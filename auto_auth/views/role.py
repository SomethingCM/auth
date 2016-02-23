#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from automation.common.CommonPaginator import SelfPaginator
from auto_auth.views.permission import PermissionVerify

from auto_auth.forms import RoleGroupForm
from auto_auth.models import RoleGroup

@login_required
@PermissionVerify()
def AddRole(request):
#添加url权限
    if request.method == "POST":
        form = RoleGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleGroupForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/role.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListRole(request):
#列出url权限
    mList = RoleGroup.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('auto_auth/role.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditRole(request,ID):
#编辑url权限
    iRole = RoleGroup.objects.get(id=ID)

    if request.method == "POST":
        form = RoleGroupForm(request.POST,instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleGroupForm(instance=iRole)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/role.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteRole(request,ID):
#删除url权限
    RoleGroup.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listroleurl'))
