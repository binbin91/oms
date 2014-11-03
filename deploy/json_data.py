# -*- coding: utf-8 -*-
import json
import os

class BuildJson(object):
    '''
    Build JSON data(base and minion_id etc..)
    '''
    def base_data(self,args):
        '''
        build base data
        '''
        info = {}
        ret = dict(info,**args)
        self.write_data('base',ret)

    def build_data(self,id,args):
        if not os.path.exists('/home/api/pillar/%s' % (id)):
            with open('/home/api/pillar/base') as f:
                obj = f.readlines()[0]
            ret = eval(obj)
            self.write_data(id,ret)
        with open('/home/api/pillar/%s' % (id)) as f:
            data = f.readlines()[0]
        cov_data = eval(data)
        if not cov_data.has_key(args.keys()[0]):
            ret = dict(cov_data,**args)
            self.write_data(id,ret)
        else:
            cov_data.update(args)
            self.write_data(id,cov_data)

    def write_data(self,file,ret):
        f = open('/home/api/pillar/%s' % (file),'w+')           
        f.write(str(ret))
        f.close()

