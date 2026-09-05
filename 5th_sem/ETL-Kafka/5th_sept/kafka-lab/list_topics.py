from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers = "localhost:9092"
)

topics = consumer.topics()

print("Available Topics :\n")
for topic in topics:
    print(topic)

consumer.close()