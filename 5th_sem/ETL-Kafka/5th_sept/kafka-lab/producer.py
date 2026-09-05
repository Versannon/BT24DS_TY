from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)


messages = [
    "Hello Kafka",
    "This is a Python producer",
    "Welcome to ETL Lab"
]

for message in messages:
    producer.send(
        "college-topic",
        message.encode("utf-8")
    )
    print("Sent: ", message)

producer.flush()

print("All messages sent succesfully!")