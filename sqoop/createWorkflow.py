#!/usr/bin/python
import sys
import os

if(len(sys.argv) < 2):
  print("Usage: " + sys.argv[0] + "oracle_tablenames_file")
  sys.exit()

oracletablenamesFile=sys.argv[1]
cnt=0

#open oracle tablenames file
try:
   with open(oracletablenamesFile,'r') as f:
       lines=f.readlines()
except:
   print('Failed to open' + oracletablenamesFile)
   sys.exit()
# Open the workflow output file for write
try:
    workflowFile=open('workflow.xml','w+');
    jobProperties=open('job.properties','w+');
except IOError:
    print('Failed to open the workflow.xml file for writing')
    sys.exit()

#add header to workflow.xml
workflowFile.write("<workflow-app name=\"${workflowName}\" xmlns=\"uri:oozie:workflow:0.5\"> \n")
workflowFile.write("    <start to=\"fork1\"/> \n")
workflowFile.write("    <kill name=\"Kill\" > \n")
workflowFile.write("        <message>Action failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message> \n")
workflowFile.write("    </kill> \n")
workflowFile.write("    <fork name=\"fork1\"> \n")

#add header to job.properties

jobProperties.write("workflowName=wfl_sqoop\n")
jobProperties.write("nameNode=hdfs://nameservice1\n")
jobProperties.write("jobTracker=yarnRM\n")
jobProperties.write("hcatUri=thrift://dev-r01edge.c21.hadoop.td.com:9083\n")
jobProperties.write("hcatPrinciple=hive/hiveserver.c21.hadoop.td.com@C21.HADOOP.TD.COM\n")
jobProperties.write("oozie.use.system.libpath=true\n")
jobProperties.write("timezone=America/Toronto\n")
jobProperties.write("jdbcURL=jdbc:hive2://hiveserver.c21.hadoop.td.com:10000/default;principal=hive/hiveserver.c21.hadoop.td.com@C21.HADOOP.TD.COM\n")
jobProperties.write("password=tdiimcontrol107\n")
jobProperties.write("wfroot=${nameNode}/share/catdiim01/dev7/scripts/sqoop\n")
jobProperties.write("oozie.wf.application.path=${wfroot}/workflow.xml\n")
jobProperties.write("user=appscatdiim01\n")
jobProperties.write("tablesDirectory=/share/catdiim01/dev7/stage_g0070\n")



#add fork for each table and variables in the job.footer which will later be incorporated into job.properties
for line in lines:
  cnt=cnt+1 
  workflowFile.write("      <path start=\"sqoopJob"  +str(cnt)+ "\"/> \n")
  jobProperties.write("tablename"+str(cnt)+ "=" + line.upper())
  jobProperties.write("target_dir"+str(cnt)+ "=" + line.lower()) 

workflowFile.write("     </fork> \n")
jobProperties.close()

#add action for each table

cnt=0
for line in lines:
  cnt=cnt+1

  workflowFile.write("  <action name=\"sqoopJob" +str(cnt)+ "\">\n")
  workflowFile.write("      <sqoop xmlns=\"uri:oozie:sqoop-action:0.2\"> \n")
  workflowFile.write("          <job-tracker>${jobTracker}</job-tracker>\n")
  workflowFile.write("          <name-node>${nameNode}</name-node>\n")
  workflowFile.write("          <configuration>\n")
  workflowFile.write("              <property>\n")
  workflowFile.write("                  <name>mapred.compress.map.output</name>\n")
  workflowFile.write("                  <value>true</value>\n")
  workflowFile.write("              </property>\n")
  workflowFile.write("          </configuration>\n")
  workflowFile.write("          <arg>import</arg>\n")
  workflowFile.write("          <arg>--connect</arg>\n")
  workflowFile.write("          <arg>jdbc:oracle:thin:@10.155.22.41:1515:DEVHMG44</arg>\n")
  workflowFile.write("          <arg>--username</arg>\n")
  workflowFile.write("          <arg>talend_dev7</arg>\n")
  workflowFile.write("          <arg>--password</arg>\n")
  workflowFile.write("          <arg>${password}</arg>\n")
  workflowFile.write("          <arg>--table</arg>\n")
  workflowFile.write("          <arg>${tablename" +str(cnt) +"}</arg>\n")
  workflowFile.write("          <arg>--target-dir</arg>\n")
  workflowFile.write("          <arg>${tablesDirectory}/${target_dir"+str(cnt) +"}</arg>\n")
  workflowFile.write("          <arg>--delete-target-dir</arg>\n")
  workflowFile.write("          <arg>-m</arg>\n")
  workflowFile.write("          <arg>1</arg>\n")
  workflowFile.write("      </sqoop>\n")
  workflowFile.write("     <ok to=\"join1\"/>\n")
  workflowFile.write("     <error to=\"Kill\"/>\n")
  workflowFile.write("  </action>\n")


#add footer
workflowFile.write("   <join name=\"join1\" to=\"End\" /> \n")
workflowFile.write("   <end name=\"End\"/> \n")
workflowFile.write("</workflow-app> \n")


#close the file and exit
workflowFile.close()
exit(0)
