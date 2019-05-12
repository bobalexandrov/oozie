1. copy the xml and hql to hdfs : /share/catdiim01/dev7/scripts
2. set the OOZI_URL : export OOZIE_URL=https://dev-r01edge.c21.hadoop.td.com:11443/oozie
3. run the job: oozie job -config job.properties -run
4. check the status: oozie job -info {ID}, where {ID} is the ID printed on screen after the successful start
