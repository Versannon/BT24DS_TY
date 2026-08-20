# Experiment 6: Java program to create a Kafka consumer

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
