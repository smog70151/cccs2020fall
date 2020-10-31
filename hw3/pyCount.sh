hdfs dfs -rm -r -f py_wordcount

# /home/hadoop-3.1.2/share/hadoop/tools/sources
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-D mapred.map.tasks=4 \
	-mapper "$PWD/mapper.py" \
	-file "mapper.py" \
	-reducer "$PWD/reducer.py" \
	-file "reducer.py" \
	-input "wordcount" \
	-output "py_wordcount"

# Output Hadoop Log File
# mkdir hw3-log
rm -rf hw3-log/py_wordcount
hadoop fs -copyToLocal py_wordcount hw3-log
