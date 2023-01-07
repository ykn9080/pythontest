from confluent_kafka import Consumer
from flask import Flask, render_template

app = Flask(__name__)
################
c=Consumer({'bootstrap.servers':'imcmaster.iptime.org:29093','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)



def consumer_once():
    c.subscribe(['registered_user'])
    msg=c.poll(1.0) #timeout
    if msg is None:
        print('No message received')
        return
    else:
        data=msg.value().decode('utf-8')
        print(data)
        c.close()
        return data
    

def consumer_looping():
    c.subscribe(['registered_user'])
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
        return data
    # c.close()
    

if __name__ == "__main__":
    consume_loop()()