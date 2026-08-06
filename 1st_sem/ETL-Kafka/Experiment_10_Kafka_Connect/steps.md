# Experiment 10: Introduce Kafka Connect

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
