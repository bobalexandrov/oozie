#!/bin/sh
filename=/user/dataexplorer1/files/qafile_$(date +%b%d%y%s)
hdfs dfs -put /etc/passwd ${filename}

exit 0 
