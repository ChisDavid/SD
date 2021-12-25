#!/usr/bin/env python
import datetime
import sys

import pika, os
import pandas as pd
import time
import json

df = pd.read_csv('sensor.csv')

def getDataFromLine(index):
    return df.at[index,'0']


def sendData ():
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://hstxfzri:VjGRBiIpdgPB-ZAWVhAEci-boT7QUlUT@roedeer.rmq.cloudamqp.com/hstxfzri')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    queue='queue'
    channel.queue_declare(queue=queue)  # Declare a queue
    for i in range(df.shape[0]):
        value = getDataFromLine(i)
        data_set = {'sensorId':sys.argv[1],"value" : value }
        jsonData = json.dumps(data_set)
        print(jsonData)
        channel.basic_publish(exchange='',routing_key=queue,body=jsonData)
        time.sleep(3)

    print(" [x] Sent 'Hello World!'")
    connection.close()


sendData()

