# Experiment 8: Simulate fault tolerance

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
