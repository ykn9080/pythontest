from faker import Faker
from confluent_kafka import Producer
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

def push_producer(data):
   
    #data = get_registerd_data()
	#str = json_serializer(data)
    str = json.dumps(data).encode("utf-8")
    #text = "안녕"  # text는 str이 됩니다.
    #text_byte = text.encode('utf-8')
    #text_str = text_byte.decode('utf-8')
    text_str = str.decode('utf-8')
    print(text_str)
    p.poll(0)
    p.produce('registered_user', text_str)
    #time.sleep(3)
p = Producer({'bootstrap.servers':'59.13.200.115:29093'})
# p = Producer({'bootstrap.servers':'localhost:29092'})

if __name__ == "__main__":
    while True:
        data = get_registerd_data()
	#str = json_serializer(data)
        str = json.dumps(data).encode("utf-8")
        #text = "안녕"  # text는 str이 됩니다.
        #text_byte = text.encode('utf-8')
        #text_str = text_byte.decode('utf-8')
        text_str = str.decode('utf-8')
        print(text_str)
        p.poll(0)
        p.produce('registered_user', text_str)
        time.sleep(3)
