# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pika

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sendToQueue(queueName):
    credentials = pika.PlainCredentials('guest','guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=8080,virtual_host='/',credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='queue')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sendToQueue("dasas")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
