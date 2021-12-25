import sys
import time

import pika, os
import json

import requests

url = os.environ.get('CLOUDAMQP_URL', 'amqps://hstxfzri:VjGRBiIpdgPB-ZAWVhAEci-boT7QUlUT@roedeer.rmq.cloudamqp.com/hstxfzri/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

localHost = 'http://localhost:8080/'
herokuHost = 'https://davidchis2021.herokuapp.com/'
url = f'{localHost}Sensor/AddData'

headers = {'Content-Type': 'application/json',"Access-Control-Allow-Origin": "*"}

def sendToBackEnd(url,obj):
    requests.post(url,obj,headers=headers)


def callback(ch, method, properties, body):
    jsonObj = json.loads(body)
    print(list(jsonObj.values())[0])

    body ={
    "sensorId":str(1),
    "value":str(list(jsonObj.values())[0])
    }
    sendToBackEnd(url,json.dumps(body))
    sendToBackEnd()

channel.basic_consume('hello', callback, auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()