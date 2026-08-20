# Experiment 12: Kafka integration with Hadoop ecosystem

## Overview
Integrating Kafka with Hadoop typically involves moving streaming data from Kafka topics into HDFS (Hadoop Distributed File System) for batch processing, or reading from HDFS into Kafka.

## Steps (Conceptual using Kafka Connect)

The most robust way to integrate Kafka and Hadoop is using **Kafka Connect** with the **HDFS Sink Connector**.

1. **Setup Hadoop:**
   Ensure you have a running Hadoop cluster (can also be set up via Docker).

2. **Install HDFS Connector:**
   Install the Confluent HDFS Sink Connector into your Kafka Connect cluster.

3. **Configure the HDFS Sink Connector:**
   Submit a JSON configuration to your Kafka Connect REST API:
   ```json
   POST http://localhost:8083/connectors
   {
     "name": "hdfs-sink",
     "config": {
       "connector.class": "io.confluent.connect.hdfs.HdfsSinkConnector",
       "tasks.max": "1",
       "topics": "my-topic",
       "hdfs.url": "hdfs://hadoop-namenode:9000",
       "flush.size": "3",
       "key.converter": "org.apache.kafka.connect.storage.StringConverter",
       "value.converter": "org.apache.kafka.connect.storage.StringConverter"
     }
   }
   ```

4. **Verify Integration:**
   Produce messages to `my-topic` in Kafka. Once the `flush.size` threshold is reached (e.g., 3 messages), the connector will write the data to an HDFS file.
   Use the Hadoop CLI to check the files:
   ```bash
   hdfs dfs -ls /topics/my-topic/
   hdfs dfs -cat /topics/my-topic/partition=0/*
   ```
