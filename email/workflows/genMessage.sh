#!/bin/sh
workflow_name=$1
echo "Please be advised your workflow ${workflow_name} screwed up" | hdfs dfs -put -f - /user/dataexplorer1/oozie/email/workflows/message.txt
