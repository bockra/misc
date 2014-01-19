#!/bin/bash
#
# scrip for making full copy of your kindle, connected via USB
#

#default mount point of your Kindle. This one is for Os X
dir='/Volumes/Kindle'

#place for backups. I prefer to save it on my Yandex.Disk folder
bc_dir='/Users/bockra/Documents/Ya.Disk/bckp'

backup() {

#create an archive with the name : kindle_monthnumber_date.tar.gz 
tar -pvczf $bc_dir/kindle_`date "+%m_%d"`.tar.gz $dir

}

#checking for existance of Kindle connection
if [ -d $dir ] ; then
	echo "yes"
	backup
else
	echo "no Kindle connected"
fi
