#!/bin/sh
spark-submit --driver-memory 4G  --conf spark.dynamicAllocation.maxExecutors=5 --num-executors 5 --executor-cores 6 --executor-memory 4G --queue root.users.dataexplorer1 lib/cbaSparkTest.jar "settings.ini" "DEBUG" 
