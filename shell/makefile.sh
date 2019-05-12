#!/bin/sh
filename=/user/dataexplorer1/files/testfile_$(date +%b%d%y%s)

hdfs dfs -put /etc/passwd ${filename}
hdfs dfs -chown dataexplorer1 ${filename} 

exit 0 
