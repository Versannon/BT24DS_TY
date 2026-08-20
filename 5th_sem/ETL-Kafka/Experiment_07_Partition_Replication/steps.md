# Experiment 7: Topic with specific partition and replication factor

## Steps

1. **Create Topic Script:**
   You can write a simple shell script (`create_topic.sh`) or just run the command directly.

   To create a topic with explicitly specified partitions and replication factor (e.g., 3 partitions, replication factor 2):

   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh \
     --create \
     --topic advanced-topic \
     --partitions 3 \
     --replication-factor 2 \
     --bootstrap-server localhost:9092
   ```
   *(Note: Replication factor of 2 requires at least 2 Kafka brokers running in your cluster. If you only have 1 broker, this will fail. Scale up using `docker-compose up --scale kafka=2` first.)*

2. **Verify Configuration:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics.sh --describe --topic advanced-topic --bootstrap-server localhost:9092
   ```
   The output will show the details for each partition, including the `Leader`, `Replicas`, and `Isr` (In-Sync Replicas).
