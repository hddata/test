python需要安装的模块有smtplib，string，os，urllib, urllib2，email,time
确保已经安装
test.sh 文件里
PATH="$PATH":/usr/local/python-2.7.11/bin
因为升级过python，所以这里要python的绝对路径
pwd_='/root/ogg_smtplib'
pwd_是整个脚本的路径
定时器格式
* * * * * cmd
分别是 ：分钟 小时 月份 星期几 命令
crontab -e
*/1 * * * * sh /root/ogg_smtplib/test.sh