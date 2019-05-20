#!/bin/sh

DIR=/share/catdiim01/dev7/scripts/sqoop

hdfs dfs -put -f workflow.xml ${DIR}

hdfs dfs -ls -R ${DIR}

oozie job -run -config job.properties

