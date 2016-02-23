#!/usr/bin/env python
#-*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from automation.common.CommonPaginator import SelfPaginator
from auto_auth.views.permission import PermissionVerify
from auto_auth.models import AuthUser,RoleGroup,PermissionList
from django.contrib import auth
from django.contrib.auth import get_user_model
from auto_auth.forms import LoginUserForm,ChangePasswordForm,AddUserForm,EditUserForm,AddAuthUserForm,EditAuthUserForm

def LoginUser(request):
    '''用户登录view'''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/autoAuth/home')

    if request.method == 'GET' and request.GET.has_key('next'):
        next = request.GET['next']
    else:
        next = '/autoAuth/home'

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm()

    kwvars = {
        'request':request,
        'form':form,
        'next':next,
    }

    return render_to_response('auto_auth/login.html',kwvars,RequestContext(request))

@login_required
#退出
def LogoutUser(request):
    auth.logout(request)
    # print request.META.get('HTTP_REFERER', '/')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect('/')



@login_required
def ChangePassword(request):
    # print request.META.get('HTTP_REFERER', '/')
    if request.method=='POST':
        form = ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('logouturl'))
            return HttpResponseRedirect('/login')
    else:
        form = ChangePasswordForm(user=request.user)

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/password.change.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
#列出用户
def ListUser(request):
    mList = get_user_model().objects.all()
    # print mList
    #分页功能
    lst = SelfPaginator(request,mList, 20)
    # print lst
    kwvars = {
        'lPage':lst,
        'request':request,
    }

    # return render_to_response('auto_auth/user.list.html',kwvars)
    return render_to_response('auto_auth/user.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
#添加用户
def AddUser(request):

    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = AddUserForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/user.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
#编辑用户
def EditUser(request,ID):
    user = get_user_model().objects.get(id = ID)

    if request.method=='POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = EditUserForm(instance=user)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/user.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
#删除用户
def DeleteUser(request,ID):
    if ID == '1':
        return HttpResponse(u'超级管理员不允许删除!!!')
    else:
        get_user_model().objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listuserurl'))

@login_required
@PermissionVerify()
#废弃
def ResetPassword(request,ID):
    user = get_user_model().objects.get(id = ID)

    newpassword = get_user_model().objects.make_random_password(length=10,allowed_chars='abcdefghjklmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789')
    print '====>ResetPassword:%s-->%s' %(user.username,newpassword)
    user.set_password(newpassword)
    user.save()

    kwvars = {
        'object':user,
        'newpassword':newpassword,
        'request':request,
    }

    return render_to_response('auto_auth/password.reset.html',kwvars,RequestContext(request))

	 
	
@login_required
@PermissionVerify()
def ListauthUser(request):
#列出auth用户
    mList = AuthUser.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('auto_auth/authuser.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def AddauthUser(request):
#添加auth用户
    if request.method=='POST':
        form = AddAuthUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.set_password(form.cleaned_data['password'])

            form.save() 
            return HttpResponseRedirect(reverse('listauthuserurl'))
    else:
        form = AddAuthUserForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/authuser.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditauthUser(request,ID):
#编辑auth用户
    auser = AuthUser.objects.get(id = ID)
    print auser
    if request.method=='POST':
        form = EditAuthUserForm(request.POST,instance=auser)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listauthuserurl'))
    else:
        form = EditAuthUserForm(instance=auser)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('auto_auth/authuser.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteauthUser(request,ID):
#删除auth用户
    ID1 = AuthUser.objects.get(id = ID).user.id
    if ID1 == '1':
        return HttpResponse(u'超级管理员不允许删除!!!')
    else:
        get_user_model().objects.filter(id = ID1).delete()
        AuthUser.objects.filter(id = ID).delete()
    return HttpResponseRedirect(reverse('listauthuserurl'))