oms
===

OMS运维管理平台

写在前言：
  分享，平台里的东西是采用各家之精华，自己融合才有了那么个东西，发表OMS博客那天，答应过后续开源，那么今天就把它分享出来
  学习，自我赶脚代码不是很好，分享出来; 希望得到学习，毕竟闭门造车不好嘛。希望得到反馈，谢谢~
  总结，从13年底就想写这么个东西，刚好下半年有空，就利用9月份把这个写了，算是对自动化运维一个小小总结，里面还有不够好的地方，希望可以得到交流，毕竟每人角度不一，观点也不一样。
        感谢蝴蝶运维老大支持，小马哥代码指点迷津，绿肥在OMS平台写的时候提供帮助~

  redhat.binbin@gmail.com   //欢迎来件~,TKS ALL~

功能简介：
installed App: 系统安装、安装记录
deploy App: Salt Key管理、模块部署、远程管理、代码发布
asset App: 主机列表、服务器软硬资产、网络设备资产、数据中心资产 

设计流程：
     传送门：http://binbin158.blog.51cto.com/2659767/1561175

安装
1.Cobbler(OMS需要调用cobbler代码模块)
     yum localinstall /tmp/cobbler-2.6.3-1.el6.noarch.rpm //  yum install cobbler

2.Saltstack
     rpm -ivh http://mirrors.sohu.com/fedora-epel/6/x86_64/epel-release-6-8.noarch.rpm
     yum install salt-master            //最近epel源有问题，可以上官网直接下载代码install

3.Saltstack API、配置
     传送门：http://pengyao.org/salt-api-deploy-and-use.html

4.MySQL-python
     yum install MySQL-python

5.MySQL安装配置(OMS数据模型、APP代码需要调用)，只要python manage.py validate没问题就OK
     1.新装一个MySQL
     2.使用现用滴， 这个环节我就略了~

6.salt_event_to_mysql.py
     传送门：http://pengyao.org/saltstack_master_retuner_over_event_system.html

7.ext_pillar(oms.py)
     传送门：http://binbin158.blog.51cto.com/2659767/1570433

配置(根据环境自行配置)：
     settings.py 数据库信息
     settings_local.py API接口信息，数据库信息
     cobble_api.py  连接信息

启动
1.导入数据类型
  mysql -uroot -p -e 'create database oms;'
  python manage.py validate
  python manage.py syncdb 

2.启动程序
  a#直接启动， python manage.py runserver 0.0.0.0:8000
  b#nginx + uwsgin，参考链接：http://binbin158.blog.51cto.com/2659767/1569298
