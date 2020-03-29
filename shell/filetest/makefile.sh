#!/bin/sh
filename=/user/dataexplorer1/files/testfile_$(date +%b%d%y%s)

hdfs dfs -put /etc/passwd ${filename}

exit 0 
