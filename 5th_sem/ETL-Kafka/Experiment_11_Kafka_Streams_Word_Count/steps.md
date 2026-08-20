# Experiment 11: Simple word count using Kafka Streams

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
               .flatMapValues(textLine -> Arrays.asList(textLine.toLowerCase().split("\\W+")))
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
