# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bson.binary import Binary
from scrapy.exceptions import DropItem
import pymongo
import logging


class ScraperPipeline:
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        # Pull settings from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'scrapy_db'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION', 'scraped_data')
        )

    def open_spider(self, spider):
        # Open MongoDB connection when spider starts
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # Close MongoDB connection when spider ends
        self.client.close()

    def process_item(self, item, spider):
        return item

    def process_item(self, item, spider):
        content = item.get('content')

        # Check if content is in binary format (PDF) or needs conversion (HTML)
        if isinstance(content, str):
            # Convert HTML content (str) to binary format
            content = content.encode('utf-8')
        elif isinstance(content, bytes):
            # Content is already in binary format (PDF), no need to convert
            pass
    
        # Wrap the binary content in MongoDB's Binary type
        item['content'] = Binary(content)

        try:
            # Insert the modified item into the MongoDB collection
            self.db[self.mongo_collection].insert_one(dict(item))
        except Exception as e:
            raise DropItem(f"Failed to insert item: {e}")
        
        return item