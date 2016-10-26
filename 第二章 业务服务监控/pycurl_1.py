# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   pycurl_1.py
    @linux:       redhat6.3
    @CreateTime:  2016/10/25 14:24
    @Description:
实现探测web服务质量

pip install pycurl
出现错误：Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-bXlbL0/pycurl/
yum install libcurl-devel
pip install pycurl
improt pycurl
出现错误：ImportError: pycurl: libcurl link-time ssl backend (nss) is different from compile-time ssl backend (none/other)
pip uninstall pycurl
export PYCURL_SSL_LIBRARY=nss  此处的nss是上一个错误括号的参数nss
pip install pycurl
重启python可正常导入
"""

import os,sys
import time
import pycurl

URL = "http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)


c.setopt(pycurl.FORBID_REUSE, 1)

c.setopt(pycurl.MAXREDIRS, 1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception, e:
    print "connection error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print"HTTP状态码： %s" %(HTTP_CODE)
print"DNS解析时间： %.2f ms" %(NAMELOOKUP_TIME*1000)
print"建立连接时间： %.2f ms" %(CONNECT_TIME*1000)
print"准备传输时间： %.2f ms" %(PRETRANSFER_TIME*1000)
print"传输开始时间： %.2f ms" %(STARTTRANSFER_TIME*1000)
print"传输结束总时间： %.2f ms" %(TOTAL_TIME*1000)
print"下载数据包大小： %d bytes/s" %(SIZE_DOWNLOAD)
print"HTTP头部大小： %d byte" %(HEADER_SIZE)
print"平均下载速度： %d bytes/s" %(SPEED_DOWNLOAD)

indexfile.close()
c.close()



