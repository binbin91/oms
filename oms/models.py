# -*- coding: utf-8 -*-
from django.db import models

class Users(models.Model):
    """
    OMS User Manage
    """
    username = models.CharField(max_length=30, verbose_name=u'用户名')
    password = models.CharField(max_length=30, verbose_name=u'密码')
 
    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'用户信息'
        verbose_name = u'用户信息管理'

class Message(models.Model):
    """
    Platform audit information
    """
    audit_time = models.DateTimeField(auto_now_add=True, verbose_name=u'时间')
    type = models.CharField(max_length=10, verbose_name=u'类型')
    action = models.CharField(max_length=10, verbose_name=u'动作') 
    action_ip = models.CharField(max_length=15, verbose_name=u'执行IP')
    content = models.CharField(max_length=50, verbose_name=u'内容')

    class Meta:
        verbose_name = u'审计信息'
        verbose_name = u'审计信息管理'
