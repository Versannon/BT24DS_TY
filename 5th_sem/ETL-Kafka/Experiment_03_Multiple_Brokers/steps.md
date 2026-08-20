# Experiment 3: Extend the cluster to multiple brokers on a single node

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
