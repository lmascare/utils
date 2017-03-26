# Tips for Apache kafka

## Concepts
**Kafka is run on a cluster of one or more servers**
**Kafka Cluster stores streams of records in categories called topics**
**Each record consists of a key, value & timestamp**

## Kafka has 4 Core APIs**
  i.    Producer 
  ii.   Consumer
  iii.  Streams
  iv.   Connector 

*Kafka requires zookeeper*
    *Zookeeper runs on port 2181*
    *Kafka runs on port 9092*

**To start & test the Kafka Server**
    1. Start zookeeper
       * cd /u/kafka
       * ./bin/zookeeper-server-start.sh config/zookeeper.properties

    2. Start kafka
       * cd /u/kafka
       * ./bin/kafka-server-start.sh config/server.properties

    3. Create a Topic
       > cd /u/kafka
       > ./bin/kafka-topics.sh --create --zookeeper localhost:2181 \
       > --replication-factor 1 --partitions 1 --topic test
       >
       > Can we see the topic
       > ./bin/kafka-topics.sh --list --zookeeper localhost:2181
