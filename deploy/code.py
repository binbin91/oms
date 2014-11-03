# -*- coding: utf-8 -*-
from subprocess import Popen,PIPE,STDOUT,call
import os

class Code_Work(object):
    def __init__(self,pro,url,ver):
        self.__pro = pro
        self.__url = url
        self.__ver = ver
        path = {'tg': 'opt/www/v', 'hdworkers': 'home/hpn'}
        self.__tgt = path[self.__pro]

    def pull_code(self):
        '''
        From the pull of gitlab project code
        '''
        ret = {
            'result': True,
            'comment': [],
        }
        if os.path.isdir('/home/work'):
            os.system('rm -rf /home/work/*')      #每次拉取,work都是干净目录
            os.chdir('/home/work')
        else:
            os.mkdir('/home/work')
            os.chdir('/home/work')
        args = 'git clone %s %s' % (self.__url,self.__tgt)                
        try:                    
            obj = Popen(args, shell=True, stdout=PIPE, stderr=STDOUT)
            ret['comment'].append(obj.stdout.readlines())
        except Exception, e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret

    def build_rpm(self):
        '''
        Project of the latest code into the RPM
        '''
        ret = {
            'result': True,
            'comment': [],
        }
        f_args = 'fpm -s dir -t rpm -n %s --epoch 0 -v %s -C /home/work -p /mirros/package %s' % (self.__pro,self.__ver,self.__tgt)
        try:
            obj = Popen(f_args, shell=True, stdout=PIPE, stderr=STDOUT)
            ret['comment'].append(obj.stdout.readlines())
        except Exception, e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret

    def push_repo(self):
        '''
        push to yum warehouse
        '''
        ret = {
            'result': True,
            'comment': [],
        }
        c_args = 'createrepo /mirros/package'
        try:
            obj = Popen(c_args, shell=True, stdout=PIPE, stderr=STDOUT)
            ret['comment'].append(obj.stdout.readlines())
        except Exception, e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret

    def work(self):
        ret = {
            'comment': [],
        }
        ret['comment'].append(self.pull_code())
        ret['comment'].append(self.build_rpm())
        ret['comment'].append(self.push_repo())
        return ret

def main():
    capi = Code_Work(pro=,url=,ver=)
    print capi.work()
    #print capi.pull_code()
    #print capi.build_rpm()
    #print capi.push_repo()

if __name__ == '__main__':
    main()
