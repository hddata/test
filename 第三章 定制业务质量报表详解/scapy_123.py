# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   scapy_123.py -v1.0
    @Author:      cnshhi
    @CreateTime:  2016/11/1 13:30
    @Description:
    探测机到目标服务器的路由轨迹
"""
# yum install tcpdump graphviz ImageMagick
#pip install scapy
import warnings,logging
import os,sys,time,subprocess
warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import traceroute

domains = raw_input('Please input one or more IP/domain:')
target = domains.split(' ')
dport = [80]
if len(target) >= 1 and target[0]!='':
    res,ans= traceroute(target,dport=dport,retry=-2)
    res.graph(target="> test.svg")
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True)
else:
    print "IP/domain number of ettort,exit"
