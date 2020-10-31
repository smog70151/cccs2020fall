#!/bin/bash

# Env. Set up
export HADOOP_CLASSPATH=$(hadoop classpath)
# Compile
javac -classpath ${HADOOP_CLASSPATH} -d . HadoopWordCountSample.java
# Package
jar cf hwcs.jar HadoopWordCountSample*.class


hdfs dfs -rm -r -f java_wordcount
hadoop jar hwcs.jar HadoopWordCountSample wordcount java_wordcount

# Dump Data from HDFS
rm -rf hw3-log/java_wordcount
hadoop fs -copyToLocal java_wordcount hw3-log

# Free tmpFiles
rm -rf HadoopWordCountSample*.class
rm -rf hwcs.jar
