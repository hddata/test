# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   nmap_1.py -v1.0
    @Author:      cnshhi
    @CreateTime:  2016/11/2 11:05
    @Description:
    实现高效的端口扫描
"""


""" yum -y install nmap
    pip install python-nmap

"""

import sys
import nmap

scan_raw=[]
input_data = raw_input('Please input hosts and port: ')
scan_raw = input_data.split(" ")
if len(scan_raw)!= 2:
    print "Input errors,example \"192.168.1.0/24 80,443,22\""
    sys.exit(0)
hosts=scan_raw[0]
port=scan_raw[1]

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print ('Nmap not found ',sys.exc_info()[0])
    sys.exit(0)
except:
    print ("Unexpected error:",sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)
except Exception,e:
    print "Scan ettor:"+str(e)

for host in nm.all_hosts():
    print '---------------------------------------'
    print 'Host : %s (%s)'% (host, nm[host].hostname())
    print 'State : %s'% nm[host].state()
    for proto in nm[host].all_protocols():
        print '---------'
        print 'Portocol :%s' % proto

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print 'port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])