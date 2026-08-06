# Experiment 2: Single-node, single-broker basic operations

Demonstrate setting up a single-node, single-broker Kafka cluster and show basic operations such as creating topics and producing/consuming messages.

## Steps

*Note: Replace `<kafka_container_name>` with the actual name of your Kafka container (e.g., `etl-kafka-kafka-1`).*

1. **Create a Topic:**
   Open a terminal and run the following command to execute the topic creation script inside the Kafka container:
   ```bash
   docker exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic hello-world --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

2. **List Topics:**
   Verify the topic was created:
   ```bash
  docker exec kafka /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   ```

3. **Produce Messages:**
   Start the interactive console producer:
   ```bash
   docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh --topic hello-world --bootstrap-server localhost:9092
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
   docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh --topic hello-world --from-beginning --bootstrap-server localhost:9092
   ```
   You should see the messages you typed earlier.
