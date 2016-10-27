#! /bin/bash
PATH="$PATH":/usr/local/python-2.7.11/bin
pwd_='/root/ogg_smtplib'
cd $pwd_
sh $pwd_/ogg_ssh_status.sh hostlist ogg_status.sh &>$pwd_/ogg.log
python $pwd_/smtplib_2.py
rm -rf $pwd_/ogg.log
