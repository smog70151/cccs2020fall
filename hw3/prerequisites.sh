#!/bin/bash
# Download Requirement 
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
wget https://archive.apache.org/dist/hbase/1.4.9/hbase-1.4.9-bin.tar.gz
wget https://archive.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz
wget https://github.com/cloudera/hue/archive/release-4.3.0.tar.gz
wget http://archive.apache.org/dist/hive/hive-2.3.4/apache-hive-2.3.4-bin.tar.gz

# Java & Scala 
sudo apt install default-jdk
sudo apt-get install scala

# Docker env
sudo docker build -t hadoop3hbase-spark-hive .
sudo docker pull sdwangntu/hive-metastore-db
sudo docker pull sdwangntu/hadoop3hbase-spark-hive

# Execute 
sudo docker network create -d overlay --attachable my-attachable-network
sudo docker run --hostname=mysql --name mysql --network my-attachable-network -d sdwangntu/hive-metastore-db
sudo docker run --hostname=hadoop-master --name hadoop-master --network my-attachable-network -d sdwangntu/hadoop3hbase-spark-hive
sudo docker run --hostname=hadoop-worker --name hadoop-worker --network my-attachable-network -d sdwangntu/hadoop3hbase-spark-hive
sudo docker run --hostname=hadoop-dev --name hadoop-dev -v $(pwd):/home --network my-attachable-network -d sdwangntu/hadoop3hbase-spark-hive

# Go into hadoop-dev shell
# sudo docker ps -a 
# sudo docker exec -it 40aa24e4399e /bin/bash
