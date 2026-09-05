from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)


messages = [
    "Versannnonnn"
]

for message in messages:
    producer.send(
        "college-topic",
        message.encode("utf-8")
    )
    print("Sent: ", message)

producer.flush()

print("All messages sent succesfully!")