python��Ҫ��װ��ģ����smtplib��string��os��urllib, urllib2��email,time
ȷ���Ѿ���װ
test.sh �ļ���
PATH="$PATH":/usr/local/python-2.7.11/bin
��Ϊ������python����������Ҫpython�ľ���·��
pwd_='/root/ogg_smtplib'
pwd_�������ű���·��
��ʱ����ʽ
* * * * * cmd
�ֱ��� ������ Сʱ �·� ���ڼ� ����
crontab -e
*/1 * * * * sh /root/ogg_smtplib/test.sh