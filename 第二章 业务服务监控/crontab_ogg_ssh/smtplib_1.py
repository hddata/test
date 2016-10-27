# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   smtplib_1.py
    @Author:      cnshhi
    @CreateTime:  2016/10/25 10:02
    @Email:       cnshi@travelsky.com
    @Description: 
"""

import smtplib
import string
import os
HOST = "smtp.qq.com"
SUBJECT = "ogg巡检结果"
TO = "847456767@qq.com, 2104993123@qq.com"
TO = string.splitfields(TO, ",")
FROM = "847456767@qq.com"
pwd = os.getcwd()
text_ = pwd + '/ogg.log'
text = open(text_).read( )
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
    ),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("847456767@qq.com","qhindjmvswdvbffi")
server.sendmail(FROM,TO,BODY)
server.quit()
