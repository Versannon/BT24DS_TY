# Experiment 4: Write a simple Java program to create a Kafka producer

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
