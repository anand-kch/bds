# bds

hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file Downloads/wc_mapper.py  -file Downloads/wc_reducer.py -mapper "python Downloads/wc_mapper.py" -reducer "python Downloads/wc_reducer.py" -input Downloads/sample.txt -output /wc_output/wc_output
