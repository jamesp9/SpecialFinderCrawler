# -*- coding: utf-8 -*-
from kombu.pools import producers
from kombu import Exchange, Queue, Connection

scrapy_exchange = Exchange('scrapy_exchange', type='fanout')
scrapy_result_queues = [
                        # For analysing the result
                        Queue('scrapy_result_analysis', scrapy_exchange),
                        # For dumping to the database
                        Queue('scrapy_result_db', scrapy_exchange),
                       ]


class QueueDumperPipeline(object):

    def __init__(self, queue_url):
        self.queue_url = queue_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            queue_url=crawler.settings.get('QUEUE_URL')
        )

    def open_spider(self, spider):
        self.connection = Connection(self.queue_url)

    def process_item(self, item, spider):
        item_dict = {}
        for key, value in item.items():
            item_dict[key] = value

        with producers[self.connection].acquire(block=True) as producer:
            producer.publish(item_dict,
                              serializer='msgpack',
                              exchange=scrapy_exchange,
                              declare=[scrapy_exchange]+scrapy_result_queues)
        return item
