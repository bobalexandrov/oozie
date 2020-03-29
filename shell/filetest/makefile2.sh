#!/bin/sh
filename=/user/dataexplorer1/files/devfile_$(date +%b%d%y%s)

hdfs dfs -put /etc/passwd ${filename}

exit 0 
