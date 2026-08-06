import os

base_dir = r"c:\Soham\Repositories\BT24DS_TY\1st_sem\ETL-Kafka"

experiments = {
    "Experiment_01_Install_Kafka": """# Experiment 1: Install Apache Kafka on a single node

Since you have already installed Apache Kafka using Docker on Windows, this experiment is largely complete! 

## Prerequisites
- Docker Desktop running on Windows.
- `docker-compose.yml` file configured with Zookeeper and Kafka services.

## Steps to Verify Installation
1. Open a terminal (PowerShell or Command Prompt) in the directory containing your `docker-compose.yml`.
2. Start the Kafka cluster:
   ```bash
   docker-compose up -d
   ```
3. Check if the containers are running:
   ```bash
   docker ps
   ```
   You should see both Zookeeper and Kafka containers up and running.
4. To stop the cluster later, you can run:
   ```bash
   docker-compose down
   ```
""",
    "Experiment_02_Basic_Operations": """# Experiment 2: Single-node, single-broker basic operations

Demonstrate setting up a single-node, single-broker Kafka cluster and show basic operations such as creating topics and producing/consuming messages.

## Steps

*Note: Replace `<kafka_container_name>` with the actual name of your Kafka container (e.g., `etl-kafka-kafka-1`).*

1. **Create a Topic:**
   Open a terminal and run the following command to execute the topic creation script inside the Kafka container:
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

2. **List Topics:**
   Verify the topic was created:
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --list --bootstrap-server localhost:9092
   ```

3. **Produce Messages:**
   Start the interactive console producer:
   ```bash
   docker exec -it <kafka_container_name> kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
   ```
   Type some messages and press Enter:
   ```
   >Hello Kafka!
   >This is my first message.
   ```
   Press `Ctrl+C` to exit the producer.

4. **Consume Messages:**
   Open a *new* terminal window and start the console consumer to read messages from the beginning:
   ```bash
   docker exec -it <kafka_container_name> kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092
   ```
   You should see the messages you typed earlier.
""",
    "Experiment_03_Multiple_Brokers": """# Experiment 3: Extend the cluster to multiple brokers on a single node

To simulate a multi-broker cluster using Docker on a single machine, we will scale the Kafka service using `docker-compose`.

## Steps

1. **Modify `docker-compose.yml` (if necessary):**
   Ensure your `docker-compose.yml` does not map the Kafka port to a static host port (like `9092:9092`) if you want to run multiple instances, or use a Docker network to allow them to communicate internally. Often, removing the static port binding or defining a range (e.g., `9092-9094:9092`) is needed so ports don't conflict.

2. **Scale the Kafka Service:**
   Run the following command to scale the Kafka service (assuming the service is named `kafka` in your compose file):
   ```bash
   docker-compose up -d --scale kafka=3
   ```
   This will spin up 3 Kafka broker containers connected to the same Zookeeper.

3. **Verify the Brokers:**
   Check the running containers:
   ```bash
   docker ps
   ```
   You should see three Kafka containers running.

4. **Create a Topic with Multiple Replicas:**
   Now you can create a topic that spans multiple brokers:
   ```bash
   docker exec -it <any_kafka_container> kafka-topics.sh --create --topic multi-broker-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 3
   ```

5. **Describe the Topic:**
   Check the details to see how partitions and replicas are distributed among the brokers:
   ```bash
   docker exec -it <any_kafka_container> kafka-topics.sh --describe --topic multi-broker-topic --bootstrap-server localhost:9092
   ```
""",
    "Experiment_04_Java_Producer": """# Experiment 4: Write a simple Java program to create a Kafka producer

## Prerequisites
- JDK installed on your Windows machine.
- Maven or Gradle to manage dependencies (or add Kafka Clients JAR manually).

## Steps

1. **Create a Maven Project:**
   Set up a standard Java Maven project and add the following dependency to your `pom.xml`:
   ```xml
   <dependency>
       <groupId>org.apache.kafka</groupId>
       <artifactId>kafka-clients</artifactId>
       <version>3.6.0</version> <!-- Use appropriate version -->
   </dependency>
   ```

2. **Write the Producer Code:**
   Create a class `SimpleProducer.java`:
   ```java
   import org.apache.kafka.clients.producer.KafkaProducer;
   import org.apache.kafka.clients.producer.ProducerRecord;
   import org.apache.kafka.clients.producer.ProducerConfig;
   import org.apache.kafka.common.serialization.StringSerializer;

   import java.util.Properties;

   public class SimpleProducer {
       public static void main(String[] args) {
           String bootstrapServers = "127.0.0.1:9092"; // Make sure your container maps to this port
           String topic = "java-topic";

           Properties properties = new Properties();
           properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
           properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
           properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

           KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

           ProducerRecord<String, String> record = new ProducerRecord<>(topic, "key", "Hello from Java Producer!");

           producer.send(record);
           producer.flush();
           producer.close();
           System.out.println("Message sent successfully.");
       }
   }
   ```

3. **Run the Producer:**
   Compile and run the program. Make sure the topic `java-topic` exists or allow Kafka to auto-create it.

4. **Verify:**
   Use the console consumer in your Docker container to verify the message was received.
""",
    "Experiment_05_Sync_Async_Producer": """# Experiment 5: Send messages synchronously and asynchronously

## Steps

Building upon Experiment 4, we will modify the `producer.send()` method.

### 1. Asynchronous Send (Default)
By default, `producer.send()` is asynchronous. We can add a Callback to handle the response when the broker acknowledges the message.

```java
producer.send(record, new Callback() {
    @Override
    public void onCompletion(RecordMetadata metadata, Exception exception) {
        if (exception == null) {
            System.out.println("Received metadata: Topic=" + metadata.topic() + 
                               ", Partition=" + metadata.partition() + 
                               ", Offset=" + metadata.offset());
        } else {
            exception.printStackTrace();
        }
    }
});
```

### 2. Synchronous Send
To send synchronously, we call `.get()` on the Future object returned by `send()`. This blocks the thread until the broker responds.

```java
try {
    RecordMetadata metadata = producer.send(record).get(); // Blocks until response
    System.out.println("Sent synchronously to partition " + metadata.partition());
} catch (Exception e) {
    e.printStackTrace();
}
```

### 3. Run and Compare
Run both versions. You will notice that synchronous sends are slower if you are sending a loop of thousands of messages, as it waits for network round-trips for every single message.
""",
    "Experiment_06_Java_Consumer": """# Experiment 6: Java program to create a Kafka consumer

## Steps

1. **Add Dependencies:**
   Ensure `kafka-clients` is in your `pom.xml` (same as Experiment 4).

2. **Write the Consumer Code:**
   Create a class `SimpleConsumer.java`:
   ```java
   import org.apache.kafka.clients.consumer.ConsumerConfig;
   import org.apache.kafka.clients.consumer.ConsumerRecord;
   import org.apache.kafka.clients.consumer.ConsumerRecords;
   import org.apache.kafka.clients.consumer.KafkaConsumer;
   import org.apache.kafka.common.serialization.StringDeserializer;

   import java.time.Duration;
   import java.util.Arrays;
   import java.util.Properties;

   public class SimpleConsumer {
       public static void main(String[] args) {
           String bootstrapServers = "127.0.0.1:9092";
           String groupId = "my-java-application";
           String topic = "java-topic";

           Properties properties = new Properties();
           properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
           properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
           properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
           properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, groupId);
           properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

           KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);
           consumer.subscribe(Arrays.asList(topic));

           System.out.println("Waiting for messages...");
           while (true) {
               ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
               for (ConsumerRecord<String, String> record : records) {
                   System.out.println("Key: " + record.key() + ", Value: " + record.value() +
                                      ", Partition: " + record.partition() + ", Offset: " + record.offset());
               }
           }
       }
   }
   ```

3. **Run the Consumer:**
   Execute the program. It will start polling the broker and will print any messages sent to `java-topic`.
""",
    "Experiment_07_Partition_Replication": """# Experiment 7: Topic with specific partition and replication factor

## Steps

1. **Create Topic Script:**
   You can write a simple shell script (`create_topic.sh`) or just run the command directly.

   To create a topic with explicitly specified partitions and replication factor (e.g., 3 partitions, replication factor 2):

   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh \\
     --create \\
     --topic advanced-topic \\
     --partitions 3 \\
     --replication-factor 2 \\
     --bootstrap-server localhost:9092
   ```
   *(Note: Replication factor of 2 requires at least 2 Kafka brokers running in your cluster. If you only have 1 broker, this will fail. Scale up using `docker-compose up --scale kafka=2` first.)*

2. **Verify Configuration:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --describe --topic advanced-topic --bootstrap-server localhost:9092
   ```
   The output will show the details for each partition, including the `Leader`, `Replicas`, and `Isr` (In-Sync Replicas).
""",
    "Experiment_08_Fault_Tolerance": """# Experiment 8: Simulate fault tolerance

## Steps

1. **Ensure Multi-Broker Setup:**
   Ensure you have multiple Kafka brokers running (e.g., 3 brokers) and a topic created with replication factor > 1 (e.g., `multi-broker-topic` from Experiment 3).

2. **Identify the Leader:**
   Describe the topic to see which broker is the leader for Partition 0:
   ```bash
   docker exec -it <any_kafka_container> kafka-topics.sh --describe --topic multi-broker-topic --bootstrap-server localhost:9092
   ```
   Look for `Leader: X` for partition 0.

3. **Kill the Leader Broker:**
   Find the container ID or name corresponding to broker X. Stop that container using Docker:
   ```bash
   docker stop <broker_X_container_name>
   ```

4. **Observe Cluster Behavior:**
   Run the describe command again:
   ```bash
   docker exec -it <any_kafka_container> kafka-topics.sh --describe --topic multi-broker-topic --bootstrap-server localhost:9092
   ```
   You will notice that a new broker has been elected as the `Leader` for partition 0, and the old broker is no longer in the `Isr` (In-Sync Replicas) list.

5. **Verify Data Availability:**
   Start a console consumer to read from the topic. The data should still be fully available despite the broker going down, demonstrating fault tolerance.
""",
    "Experiment_09_Modify_Delete_Topics": """# Experiment 9: Modify configurations and delete topics

## Steps

1. **List Topics:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --list --bootstrap-server localhost:9092
   ```

2. **Modify Topic Configuration (Increase Partitions):**
   You can increase the number of partitions (Note: you cannot decrease partitions).
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --alter --topic test-topic --partitions 5 --bootstrap-server localhost:9092
   ```

3. **Modify Topic Configuration (Change Retention Time):**
   Use `kafka-configs.sh` to alter topic-level configurations. For example, set retention to 1 hour (3600000 ms):
   ```bash
   docker exec -it <kafka_container_name> kafka-configs.sh --alter --entity-type topics --entity-name test-topic --add-config retention.ms=3600000 --bootstrap-server localhost:9092
   ```

4. **Delete a Topic:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --delete --topic test-topic --bootstrap-server localhost:9092
   ```
   *(Note: Ensure `delete.topic.enable=true` is set in your broker configuration if using an older Kafka version).*

5. **Verify Deletion:**
   List topics again to ensure it has been removed.
""",
    "Experiment_10_Kafka_Connect": """# Experiment 10: Introduce Kafka Connect

Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems.

## Steps

1. **Start Kafka Connect:**
   Usually, Kafka Connect is run as a separate service. You can add a Kafka Connect container to your `docker-compose.yml` (using an image like `confluentinc/cp-kafka-connect`).

2. **Configure a File Source Connector:**
   We will use the standalone file source connector as a basic example. 
   Create a file `test.txt` inside the connect container with some text.

3. **Create the Connector via REST API:**
   Once Connect is running (e.g., on port 8083), use `curl` or Postman to configure it:
   ```json
   POST http://localhost:8083/connectors
   {
     "name": "local-file-source",
     "config": {
       "connector.class": "FileStreamSource",
       "tasks.max": "1",
       "file": "/tmp/test.txt",
       "topic": "connect-test"
     }
   }
   ```

4. **Verify Data in Kafka:**
   Start a console consumer on the `connect-test` topic. You should see the contents of `test.txt` streaming into the topic. If you append lines to `test.txt`, they will appear in Kafka.
""",
    "Experiment_11_Kafka_Streams_Word_Count": """# Experiment 11: Simple word count using Kafka Streams

## Prerequisites
- Java Maven project. Add the `kafka-streams` dependency.

```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
    <version>3.6.0</version>
</dependency>
```

## Steps

1. **Write the Streams Application:**
   ```java
   import org.apache.kafka.common.serialization.Serdes;
   import org.apache.kafka.streams.KafkaStreams;
   import org.apache.kafka.streams.StreamsBuilder;
   import org.apache.kafka.streams.StreamsConfig;
   import org.apache.kafka.streams.kstream.KStream;
   import org.apache.kafka.streams.kstream.KTable;
   import org.apache.kafka.streams.kstream.Produced;

   import java.util.Arrays;
   import java.util.Properties;

   public class WordCountApp {
       public static void main(String[] args) {
           Properties props = new Properties();
           props.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount-application");
           props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
           props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
           props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

           StreamsBuilder builder = new StreamsBuilder();
           KStream<String, String> textLines = builder.stream("streams-plaintext-input");

           KTable<String, Long> wordCounts = textLines
               .flatMapValues(textLine -> Arrays.asList(textLine.toLowerCase().split("\\\\W+")))
               .groupBy((key, word) -> word)
               .count();

           wordCounts.toStream().to("streams-wordcount-output", Produced.with(Serdes.String(), Serdes.Long()));

           KafkaStreams streams = new KafkaStreams(builder.build(), props);
           streams.start();
           
           Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
       }
   }
   ```

2. **Create Topics:**
   Create `streams-plaintext-input` and `streams-wordcount-output`.

3. **Run the Application:**
   Start the Java app. Produce some text sentences into the input topic. Consume from the output topic (using a Long deserializer for the value) to see the live word counts!
""",
    "Experiment_12_Hadoop_Integration": """# Experiment 12: Kafka integration with Hadoop ecosystem

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
"""
}

if not os.path.exists(base_dir):
    os.makedirs(base_dir, exist_ok=True)

for folder_name, content in experiments.items():
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "steps.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
print("Folders and steps created successfully.")
