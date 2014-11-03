# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from installed.models import *
from asset.models import HostList
from installed.form import SystemInstallForm
from installed.cobbler_api import CobblerAPI
from oms.models import *
from oms.mysql import db_operate
from oms import settings

def system_install_managed(request,id=None):
    """
    Management host to be installed
    """
    user = request.user
    if id:
        system_install = get_object_or_404(SystemInstall, pk=id)
        page_name = '编辑主机'
    else:
        system_install = SystemInstall()
        page_name = '添加主机'
    if request.method == 'POST': 
        operate = request.POST.get('operate')
        form = SystemInstallForm(request.POST,instance=system_install)
        if form.is_valid():
            if operate:
                if operate == 'update':
                    form.save()
                    db = db_operate() 
                    sql = 'select ip from installed_systeminstall where id = %s' % (id)
                    ret = db.mysql_command(settings.OMS_MYSQL,sql)
                    Message.objects.create(type='idc', action='install', action_ip=ret, content='主机信息已更新(macadd、system_version)，准备装机')
                    return HttpResponseRedirect(reverse('install_list'))
                else:
                    pass
    else:
        form = SystemInstallForm(instance=system_install)

    return render_to_response('install_manage.html',
           {"form": form,
            "page_name": page_name,
           },context_instance=RequestContext(request))   

def system_install_list(request):
    """
    List all waiting for the host operating system is installed
    """
    user = request.user

    #获取待装机的信息,从数据库中查询是否存在，未存在的插入到列表
    result = HostList.objects.filter(status='待装机')
    install_list = []
    for i in range(len(result)):
        ip = str(result[i]).split()[0]
        hostname = str(result[i]).split()[2]
        ret = SystemInstall.objects.filter(ip=ip)
        if ret:
            message = ip + ' already in database'
        else:
            data = {'ip': ip, 'hostname': hostname}
            install_list.append(data)
    
    #列表数据插入数据库 
    for i in range(len(install_list)):
        p = SystemInstall(ip=install_list[i]['ip'],hostname=install_list[i]['hostname'])
        p.save()

    all_system_list = SystemInstall.objects.all()
    paginator = Paginator(all_system_list,10)

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        all_system_list = paginator.page(page)
    except :
        all_system_list = paginator.page(paginator.num_pages)

    return render_to_response('install_list.html', {'all_system_list': all_system_list, 'page': page, 'paginator':paginator})

def system_install(request):
    """
    1.Add Some Info to Cobbler System
    2.Remote starting up
    3.screen put in System Install process //这块信息暂且空着，日后有IPMI实践补上
    """

    cobbler = CobblerAPI(url=settings.Cobbler_API['url'],username=settings.Cobbler_API['user'],password=settings.Cobbler_API['password'])    
    if request.method == 'GET':
       ip = request.GET.get('ip')
       hostname = request.GET.get('host')
       mac_add = request.GET.get('mac')
       profile = request.GET.get('ver')
       ret = cobbler.add_system(hostname=hostname,ip_add=ip,mac_add=mac_add,profile=profile)
       if ret['result']:
           data = SystemInstall.objects.filter(ip=ip)
           install_date = str(data[0]).split('--')[1].strip()
           InstallRecord.objects.create(ip=ip,system_version=profile,install_date=install_date)
           HostList.objects.filter(ip=ip).update(status='已使用')     #主机信息加入cobbler system，主机列表的状态变更为已使用状态，不再是待装机状态！
           SystemInstall.objects.filter(ip=ip).delete()               #安装后，装机列表此IP信息删除，转让到安装记录里供审计
           Message.objects.create(type='idc', action='install', action_ip=ip, content='主机信息添加至cobbler，进入安装模式')
       return HttpResponseRedirect(reverse('install_list'))
       

def system_install_record(request):
    """
    List all operating system installation records
    """
    
    user = request.user 

    record = InstallRecord.objects.all() 
    paginator = Paginator(record,10)

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        record = paginator.page(page)
    except :
        record = paginator.page(paginator.num_pages)
 
    return render_to_response('install_record_list.html', {'record': record, 'page': page, 'paginator':paginator})    
