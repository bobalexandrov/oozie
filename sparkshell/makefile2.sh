#!/bin/sh
filename=/user/dataexplorer1/files/devfile_$(date +%b%d%y%s)

hdfs dfs -put /etc/passwd ${filename}
hdfs dfs -chown dataexplorer1 ${filename} 

exit 0 
