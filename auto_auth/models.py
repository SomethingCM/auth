# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    def __unicode__(self):
        return '%s(%s)' %(self.name,self.url)    
    class Meta:
        verbose_name = 'URL权限表'
        verbose_name_plural = "URL权限表"


class RoleGroup(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList,null=True,blank=True)
    class Meta:
        verbose_name = '权限组'
        verbose_name_plural = "权限组"
    def __unicode__(self):
        return self.name
		
class AuthUser(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField(max_length=64,blank=True,null=True)
    six_choice = ((u'人妖', u'人妖'),(u'男', u'男'),(u'女', u'女'),)
    sex =  models.CharField(max_length=2,choices=six_choice,default='人妖')
    role = models.ForeignKey(RoleGroup,null=True,blank=True)
    api_key = models.CharField(max_length=200,blank=True)
    secretkey = models.CharField(max_length=200,blank=True)
    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = "用户表"
    def __unicode__(self):
        return self.user.username