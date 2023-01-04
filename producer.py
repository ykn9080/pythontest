from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()


def get_registerd_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'created_at': fake.year()
    }


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[
                         'localhost:9092'], value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        data = get_registerd_data()
        producer.send('registered_user', value=data)
        time.sleep(3)
