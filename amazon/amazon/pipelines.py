# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pr_com.models import Product

class AmazonPipeline:
    # do acc. to django model
    def __init__(self, *args, **kwargs):
        self.unique_id = ""
        self.name=""
        self.image= ""
        self.price=""
        self.stars=""
        self.feature_bullets=""
        self.rating_count=""
        self.variant_data=""

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
    #     )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        item = Product()
        item.unique_id = self.unique_id
        item.name = self.name
        item.image = self.image
        item.price = self.price
        item.stars = self.stars
        item.feature_bullets = self.feature_bullets
        item.rating_count = self.rating_count
        item.variant_data = self.variant_data
        # item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        self.unique_id =item['unique_id']
        self.name =item['name']
        self.image =item['image']
        self.price =item['price']
        self.stars =item['stars']
        self.feature_bullets =item['feature_bullets']
        self.rating_count =item['rating_count']
        self.variant_data =item['variant_data']

        return item
