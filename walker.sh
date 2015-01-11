#!/usr/bin/env bash
#simple host walker through host list in servers.list
#ex: $walker.sh 'ls /var/log/nginx/ |grep access.log*'
user='root'
list='servers.list'
for i in `cat $list`
do
#colored server output (scheme works in OS X bash)
       	echo -e "\x1B[00;32m${i}\x1B[00m"
#do some job here
      	ssh -l $user $i $@
done
