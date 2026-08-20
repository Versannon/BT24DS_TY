# Experiment 9: Modify configurations and delete topics

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
