# bds

sudo systemctl start hadoop.service
systemctl status hadoop.service

List files in hdfs -> hadoop fs -ls /
Create Directory -> hadoop fs mkdir /lab1
Check all services are running -> jps
hadoop fs -copyToLocal /lab1/input.txt
hadoop fs -copyFromLocal input.txt

find / -name hadoop*stream*


hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file ./Downloads/wc_mapper.py -mapper 'python wc_mapper.py' -file ./Downloads/wc_reducer.py -reducer 'python wc_reducer.py' -input /assignment/sample.txt -output /wc_output 


hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar \
-file ./mapper.py -mapper 'python mapper.py' \
-file ./reducer.py -reducer 'python reducer.py' \
-input /assignment/sample.txt \
-output /wc_output 


hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar \
-file ./ctd_mapper.py -mapper 'python3 ctd_mapper.py' \
-file ./ctd_reducer.py -reducer 'python3 ctd_reducer.py' \
-input /input/Crime_Data.txt \
-output /ctd_output

https://github.com/pyJbx/hadoop
