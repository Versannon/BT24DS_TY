from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "college-topic",
    bootstrap_servers ="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="college-group"
)

print ("Waiting for messages... ")

for message in consumer:
    print("Received: ", message.value.decode("utf-8"))