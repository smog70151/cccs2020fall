# Cloud Computing & Cyber Security HW3

## Prerequisites
- Clone teacher's repo. and execute the prerequisites.sh
- Enter the Hadoop-dev env. and put the apache_access.log to the hdfs
  * hdfs dfs -mkdir -p wordcount
  * hdfs dfs -copyFromLocal apache_access.log wordcount/apache_access.log
  * hdfs dfs -ls wordcount (check file exists or not)
  * mkdir hw3-log (for the dump file)

## Hadoop Streaming - Python 3
- Hadoop Streaming Practice by Python 3
- Execute the pyCount.sh and check the dump file in the hw3-log/py_wordcount folder

## Hadoop - Java
- Hadoop Practice by Java
- Execute the javaCount.sh to compile .java file and mapruduce. After finishing, please check the dump file in the hw3-log/java_wordcount folder
---
- Checker
  * $ diff hw3-log/python/log.file hw3-log/java/log.file  
