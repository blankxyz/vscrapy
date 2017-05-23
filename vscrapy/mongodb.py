# coding:utf-8
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):

    client = MongoClient(settings["MONGO_HOST"], settings["MONGO_PORT"])
    db = client[settings["MONGO_DB"]]

    def process_item(self, item, spider):
        collection = self.db['v_yesky']
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            collection.insert(dict(item))
            log.msg("program added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item