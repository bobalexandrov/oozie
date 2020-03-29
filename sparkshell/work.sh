#!/bin/sh


hdfs dfs -put -f run.sh /user/dataexplorer1/workflows/sparkshell
hdfs dfs -chmod 755 /user/dataexplorer1/workflows/sparkshell/run.sh

hdfs dfs -put -f cbaSparkTest.jar /user/dataexplorer1/workflows/sparkshell/lib

hdfs dfs -put -f runspark.xml /user/dataexplorer1/workflows/sparkshell

