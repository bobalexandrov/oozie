#!/bin/sh

hdfs dfs -put -f makefile.sh /user/dataexplorer1/workflows/shell

hdfs dfs -put -f makefile1.sh /user/dataexplorer1/workflows/shell

hdfs dfs -put -f makefile2.sh /user/dataexplorer1/workflows/shell


hdfs dfs -put -f makefile.xml /user/dataexplorer1/workflows/shell

hdfs dfs -ls /user/dataexplorer1/workflows/shell

