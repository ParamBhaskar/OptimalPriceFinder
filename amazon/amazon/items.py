# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    rating_count = scrapy.Field()
    feature_bullets = scrapy.Field()
    variant_data = scrapy.Field()
    unique_id = scrapy.Field()

class FlipItem(scrapy.Item):

    flip_name=scrapy.Field()
    flip_images = scrapy.Field()
    flip_price = scrapy.Field()
    flip_stars = scrapy.Field()
    flip_rating_count = scrapy.Field()