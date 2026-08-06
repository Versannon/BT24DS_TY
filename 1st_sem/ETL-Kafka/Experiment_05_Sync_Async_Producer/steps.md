# Experiment 5: Send messages synchronously and asynchronously

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
