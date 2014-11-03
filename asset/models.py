# -*- coding: utf-8 -*-
from django.db import models

class HostList(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    product = models.CharField(max_length=20, verbose_name=u'产品')
    application = models.CharField(max_length=20, verbose_name=u'应用')
    idc_jg = models.CharField(max_length=10, blank=True, verbose_name=u'机柜编号')
    status = models.CharField(max_length=10, verbose_name=u'使用状态')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'备注')

    def __unicode__(self):
        return u'%s - %s - %s' %(self.ip, self.hostname, self.application )
   
    class Meta:
        verbose_name = u'主机列表'
        verbose_name = u'主机列表管理'
 
class ServerAsset(models.Model):
    manufacturer = models.CharField(max_length=20, verbose_name=u'厂商')
    productname = models.CharField(max_length=30, verbose_name=u'产品型号')
    service_tag = models.CharField(max_length=80, unique=True, verbose_name=u'序列号')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU型号')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=u'CPU线程数')
    cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    mem = models.CharField(max_length=5, verbose_name='内存大小')
    disk = models.CharField(max_length=5, verbose_name='硬盘大小')
    raid = models.CharField(max_length=5, verbose_name='RAID级别')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    macaddress = models.CharField(max_length=40, verbose_name=u'MAC地址')
    os = models.CharField(max_length=20, verbose_name=u'操作系统')
    virtual = models.CharField(max_length=20, verbose_name=u'是否为虚拟机')
    idc_name = models.CharField(max_length=10, blank=True, verbose_name=u'所属机房')

    def __unicode__(self):
        return u'%s - %s' %(self.ip, self.hostname )

    class Meta:
        verbose_name = u'主机资产信息'
        verbose_name_plural = u'主机资产信息管理'

class NetworkAsset(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    manufacturer = models.CharField(max_length=20, verbose_name=u'厂商')
    productname = models.CharField(max_length=20, verbose_name=u'产品型号')
    idc_jg = models.CharField(max_length=10,blank=True, verbose_name=u'机柜编号')
    service_tag = models.CharField(max_length=30, unique=True, verbose_name=u'序列号')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'备注', default='')

    def __unicode__(self):
        return self.ip
 
    class Meta:
        verbose_name = u'网络设备资产信息'
        verbose_name_plural = u'网络设备资产信息管理'    

class IdcAsset(models.Model):
    idc_name = models.CharField(max_length=20, verbose_name=u'机房名称')
    idc_type = models.CharField(max_length=20, verbose_name=u'机房类型')
    idc_location = models.CharField(max_length=30, verbose_name=u'机房位置')
    contract_date = models.CharField(max_length=30,verbose_name=u'合同时间')
    idc_contacts = models.CharField(max_length=30, verbose_name=u'联系电话')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'备注', default='')

    def __unicode__(self):
        return self.idc_name
   
    class Meta:
        verbose_name = u'IDC资产信息'
        verbose_name_plural = u'IDC资产信息管理'    
