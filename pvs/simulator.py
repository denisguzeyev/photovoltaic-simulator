import datetime
import random
import pika
from pvs.utils import write_report, config


class PVReport(object):
    def __init__(self, meter_value):
        """Init params:
        meter_value (int) incoming value from meter
        pv_value (int) generated photovoltaic (PV) value
        result_value (int) sum if meter_value and pv_value
        """
        self.pv_value = self._get_simulated_photovoltaic_value()
        self.meter_value = meter_value
        self.result_value = self._calc_result()

    def _calc_result(self):
        """Calculate incoming meter_value supposed to be negative *(-1)
        because it is about consumption
        """
        return self.pv_value + self.meter_value*(-1)
    
    def _get_simulated_photovoltaic_value(self):
        """Provide generated photovoltaic value"""
        return random.randint(5000,9000)


class PVSimulator(object):
    """Interact with the meter and generate simulated PV power"""
    def __init__(self):
        """Init params:
        all_result (list) accumulated (total) amount of generated power (Watt)
        minus consumption obtained from meter
        """
        self.all_results = list()
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config.HOST, port=config.PORT))
        self.channel = self.connection.channel()
        self.dt_tmp_checkpoint = datetime.datetime.now()
    
    def consume(self):
        """Connect, bind and consume data from meter"""
        
        
        self.channel.exchange_declare(exchange='pv', exchange_type='fanout')

        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange='pv', queue=queue_name)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            """Ger obtained data from sender/publisher"""
            pv_report = PVReport(meter_value=int(body))
            self.all_results.append(pv_report.result_value)
            if (datetime.datetime.now() - self.dt_tmp_checkpoint).seconds >= 2:
                write_report(pv_report.__dict__,
                            total_value=sum(self.all_results))
                self.dt_tmp_checkpoint = datetime.datetime.now()

        self.channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
    
    def stop_consume(self):
        """Give up to consume data"""
        self.channel.stop_consuming()
        self.connection.close()


def main():
    """Run the consume method of PVSimulator"""
    pv_simulator = PVSimulator()
    pv_simulator.consume()


if __name__ == "__main__":
    """Start the PVSimulator from here"""
    main()










