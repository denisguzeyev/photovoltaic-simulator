import random
import pika
from pvs.utils import config


class Meter(object):
    """Public generated values of home power consumption"""

    def produce(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config.HOST, port=config.PORT))
        channel = connection.channel()
        channel.exchange_declare(exchange='pv', exchange_type='fanout')

        try:
            while True:
                message = random.randint(0,9000)
                channel.basic_publish(exchange='pv', routing_key='',
                                      body=str(message))
                print(" [x] Sent %r" % message)
        except KeyboardInterrupt:
            connection.close()
        except Exception as e:
            print(e)
        finally:
            connection.close()

def main():
    """Run the produce method of Meter"""
    pv_simulator = Meter()
    pv_simulator.produce()

if __name__ == "__main__":
    """Start the Meter from here"""
    main()
