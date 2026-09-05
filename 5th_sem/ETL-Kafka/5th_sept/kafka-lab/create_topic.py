from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers = "localhost:9092",
    client_id = "python_admin"
)

topic = NewTopic(
    name="college-topic",
    num_partitions=1,
    replication_factor = 1
)

try:
    admin_client.create_topics(new_topics=[topic])
    print("Topic created successfully!")

except Exception as e:
    print("Topic may already exist:", e)

admin_client.close()