#!/bin/sh
if [ $# -ne 1 ]
then
    echo "Oracle table name is needed "
    exit 66
fi
PASSWORD=tdiimcontrol107
ORACLE_TABLE_NAME=$(echo $1 | awk '{ print toupper($0)}')
TABLE_NAME=$(echo ${ORACLE_TABLE_NAME} | awk '{ print tolower($0)}')
TABLE_PATH=/share/catdiim01/dev7/stage_g0070/${TABLE_NAME}

sqoop import --connect jdbc:oracle:thin:@10.155.22.41:1515:DEVHMG44 --username talend_dev7 --password ${PASSWORD} \
 --table ${ORACLE_TABLE_NAME} \
 --target-dir ${TABLE_PATH} \
 --delete-target-dir \
 --num-mappers 1

