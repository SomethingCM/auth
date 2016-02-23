from django.contrib import admin
from django.contrib.auth.models import User
from auto_auth.models import *
# Register your models here.

class PermissionListAdmin(admin.ModelAdmin):
    list_display  = ('name','url') 
class RoleGroupAdmin(admin.ModelAdmin):
    list_display  = ('name',) 
class AuthUserAdmin(admin.ModelAdmin):
    list_display  = ('user','realname','sex','role','api_key','secretkey',) 
admin.site.register(PermissionList, PermissionListAdmin)
admin.site.register(RoleGroup, RoleGroupAdmin)
admin.site.register(AuthUser, AuthUserAdmin)