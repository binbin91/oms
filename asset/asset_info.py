# -*- coding: utf-8 -*-
from sys import path
if 'deploy' not in path:
    path.append(r'deploy')
from saltapi import SaltAPI
from oms import settings
import threading

asset_info = []

def get_server_asset_info(tgt):
    '''
    Salt API得到资产信息，进行格式化输出
    '''
    global asset_info
    info = []
    sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])
    ret = sapi.remote_noarg_execution(tgt,'grains.items')
    manufacturer = ret['manufacturer']
    info.append(manufacturer)
    productname = ret['productname']
    info.append(productname)
    serialnumber = ret['serialnumber'] 
    info.append(serialnumber)
    cpu_model = ret['cpu_model']
    info.append(cpu_model)
    num_cpus = int(ret['num_cpus'])
    info.append(num_cpus)
    num_gpus = int(ret['num_gpus'])
    info.append(num_gpus)
    mem_total = str(round(int(ret['mem_total'])/1000.0,))[:-2] + 'G'
    info.append(mem_total)
    disk_size = ret['disk_size']
    info.append(disk_size)
    raidlevel = ret['raidlevel']
    info.append(raidlevel)
    id = ret['id']
    info.append(id)
    lan_ip = ret['lan_ip'][0]
    info.append(lan_ip)
    lan_mac = ret['hwaddr_interfaces']['eth0']
    info.append(lan_mac)
    sys_ver = ret['os'] + ret['osrelease'] + '-' + ret['osarch']
    info.append(sys_ver)
    virtual = ret['virtual']
    info.append(virtual)
    idc_name = ret['idc_name']
    info.append(idc_name)
    asset_info.append(info)


def multitle_collect(tgt):
    global asset_info
    #全局变量置空,避免多次请求的时候返回结果叠加
    aseet_info = []
    threads = []
    loop = 0
    numtgt = len(tgt)
    for i in range(0, numtgt, 2):
        nkeys = range(loop*2, (loop+1)*2, 1)
        #实例化线程
        for i in nkeys:
            if i >= numtgt:
                break
            else:
                t = threading.Thread(target=get_server_asset_info, args=(tgt[i],))
                threads.append(t)
        #启动线程
        for i in nkeys:
            if i >= numtgt:
                break
            else:
                threads[i].start()
        #等待并发线程结束
        for i in nkeys:
            if i >= numtgt:
                break
            else:
                threads[i].join()
        loop = loop + 1
    return asset_info

'''
if __name__ == '__main__':
    print multitle_collect(['test-02', 'test-01'])
'''
