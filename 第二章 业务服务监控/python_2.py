# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Version:     python-2.7.11
    @FileName：   python_2.py
    @Author:      cnshhi
    @CreateTime:  2016/10/24 11:02
    @Description: 两字符串的差异对比
"""

import difflib
"""不需要安装，系统自带"""
"""比较两字符串差别"""
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
and string
"""
text1_lines = text1.splitlines()
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines()
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(list(diff))


"""生成HTML格式文档"""
text2_lines = text2.splitlines()
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)


import filecmp
"""比较两个文件是否相同，相同返回ture,反之false"""
filecmp.cmp("/root/simple/nginx.conf.v1","/root/simple/nginx.conf.v3")
filecmp.cmpfiles("/root/simple","/root/simple2", ['diff.html','nginx.conf.v1','nginx.conf.v2','nginx.conf.v3', 'simple3.py'])
