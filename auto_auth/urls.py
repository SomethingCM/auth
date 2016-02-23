from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('auto_auth.views',
    url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^logout/$', 'user.LogoutUser', name='logouturl'),
    url(r'^home/$', 'view.Home', name='homeurl'),

    url(r'^first/user/add/$', 'user.AddUser', name='adduserurl'),
    url(r'^first/user/list/$', 'user.ListUser', name='listuserurl'),
    url(r'^first/user/edit/(?P<ID>\d+)/$', 'user.EditUser', name='edituserurl'),
    url(r'^first/user/delete/(?P<ID>\d+)/$', 'user.DeleteUser', name='deleteuserurl'),

    url(r'^first/user/authadd/$', 'user.AddauthUser', name='addauthuserurl'),
    url(r'^first/user/authlist/$', 'user.ListauthUser', name='listauthuserurl'),
    url(r'^first/user/authedit/(?P<ID>\d+)/$', 'user.EditauthUser', name='editauthuserurl'),
    url(r'^first/user/authdelete/(?P<ID>\d+)/$', 'user.DeleteauthUser', name='deleteauthuserurl'),

    url(r'^user/changepwd/$', 'user.ChangePassword', name='changepasswordurl'),
    url(r'^first/user/resetpwd/(?P<ID>\d+)/$', 'user.ResetPassword', name='resetpasswordurl'),

    url(r'^second/role/add/$', 'role.AddRole', name='addroleurl'),
    url(r'^second/role/list/$', 'role.ListRole', name='listroleurl'),
    url(r'^second/role/edit/(?P<ID>\d+)/$', 'role.EditRole', name='editroleurl'),
    url(r'^second/role/delete/(?P<ID>\d+)/$', 'role.DeleteRole', name='deleteroleurl'),

    url(r'^permission/deny/$', 'permission.NoPermission', name='permissiondenyurl'),

    url(r'^second/permission/add/$', 'permission.AddPermission', name='addpermissionurl'),
    url(r'^second/permission/list/$', 'permission.ListPermission', name='listpermissionurl'),
    url(r'^second/permission/edit/(?P<ID>\d+)/$', 'permission.EditPermission', name='editpermissionurl'),
    url(r'^second/permission/delete/(?P<ID>\d+)/$', 'permission.DeletePermission', name='deletepermissionurl'),
)