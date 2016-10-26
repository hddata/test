# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   python_1.py
    @Author:      cnshhi
    @CreateTime:  2016/10/21 10:45
    @Email:       cnshi@travelsky.com
    @Description: 系统基础信息模块
"""

import psutil
"""获取无聊内存大小，以及已使用大小"""
mem = psutil.virtual_memory()
mem.total,mem.used
# pip install psutil
#(4012204032, 1184514048)


"""cpu完整信息"""
psutil.cpu_times()
"""user的cpu时间比"""
psutil.cpu_times().user
"""获取cpu的逻辑个数，默认logical=True4"""
psutil.cpu_count()
"""获取cpu物理个数"""
psutil.cpu_count(logical=False)


"""内存信息"""
mem = psutil.virtual_memory()
mem
"""获取内存个数"""
mem.total
"""获取空闲内存数"""
mem.free
"""获取分区情况"""
psutil.swap_memory()


"""磁盘信息"""
psutil.disk_partitions()
"""获取分区使用情况"""
psutil.disk_usage('/')
"""获取银盘总的io个数"""
psutil.disk_io_counters()
"""获取单个分区的io个数"""
psutil.disk_io_counters(perdisk=True)


"""网络信息"""
psutil.net_io_counters()
"""每个网络接口的io信息"""
psutil.net_io_counters(pernic=True)


"""当前用户信息"""
psutil.users()
"""获取开机时间，以时间戳的形式返回"""
import datetime
psutil.boot_time()
"""自然时间格式"""
datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")


"""进程信息"""
psutil.pids()
"""实例化对象，获取进程名字"""
p = psutil.Process(2121)
p.name()
"""进程bin路径,工作目录绝对路径"""
p.exe()
p.cwd()
"""进程状态,创建时间"""
p.status()
p.create_time()
datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
"""uid信息,gid信息"""
p.uids()
p.gids()
"""进程cpu时间,进程cpu亲和度"""
p.cpu_times()
p.cpu_affinity()
"""进程内存利用率,rss,vms信息"""
p.memory_percent()
p.memory_info()
"""进程io信息,socket的nameduptles列表"""
p.io_counters()
p.connections()
"""进程开启的线程数"""
p.num_threads()


"""popen类获取启动进程信息"""
from subprocess import PIPE
p = psutil.Popen(["/usr/local/python-2.7.11/bin/python", "-c", "print 'hello' "], stdout = PIPE)
p.name()
p.username()
p.communicate()
"""有点问题"""
p.cpu_times()



# pip install IPy
from IPy import IP
"""指定网段，输出该网段的ip个数以及ip清单"""
ip = IP('192.168.0.0/28')
print ip.len()
for x in ip:
    print x

ip = IP('192.168.43.26')
"""反向解析地址格式"""
ip.reverseNames()
IP('8.8.8.8').iptype()
IP('8.8.8.8').int()
"""ip转换"""
IP('8.8.8.8').strHex()
IP('8.8.8.8').strBin()
print IP(0x8080808)

"""根据ip与掩码生成网段格式"""
print IP('192.168.43.26').make_net('255.255.255.0')
print IP('192.168.43.26/255.255.255.0',make_net=True)
print IP('192.168.1.0-192.168.1.255',make_net=True)


"""不同输出格式的网段"""
IP('192.168.1.0/24').strNormal(0)
IP('192.168.1.0/24').strNormal(1)
IP('192.168.1.0/24').strNormal(2)
IP('192.168.1.0/24').strNormal(3)

"""IP和网段是否在另一个网段里"""
IP('10.0.0.0/24') < IP('12.0.0.0/24')
'192.168.1.100' in IP('192.168.1.0/24')
IP('192.168.1.0/24') in IP('192.168.0.0/16')


"""判断两个网段是否重叠,返回1表示存在重叠，0反之"""
IP('192.168.0.0/23').overlaps('192.168.1.0/24')
IP('192.168.1.0/24').overlaps('192.168.2.0')


# pip install dnspython
import dns.resolver
"""a记录查询方法"""
domain = 'www.google.com'
A = dns.resolver.query(domain,'A')
for i in A.response.answer:
    for j in i.items:
        print j.address


"""MX记录查询方法"""
domain = '163.com'
MX = dns.resolver.query(domain,'MX')
for i in MX:
    print 'MX preference = ', i.preference, 'mail exchanger =',i.exchange


"""NS记录查询记录方法"""
domain = 'baidu.com'
ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()

"""CNAME记录查询方法"""
domain = 'www.baidu.com'
cname = dns.resolver.query(domain,'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()