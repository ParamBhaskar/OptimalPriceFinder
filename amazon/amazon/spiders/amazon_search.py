import json
import scrapy
from urllib.parse import urljoin
import re
from ..items import AmazonItem
from ..items import FlipItem
from pr_com.models import Product

class AmazonSearchSpider(scrapy.Spider):
    name = "amazon_search"
    # custom_settings = {
    #     'FEEDS': { 'data/%(name)s_%(time)s.csv': { 'format': 'csv',}}
    #     }
    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.stringextra = kwargs.get('stringextra')
        # self.domain = kwargs.get('domain')
        # self.start_urls = [self.url]
        # self.allowed_domains = [self.domain]
        self.unique_id= kwargs.get('unique_id')

        super(AmazonSearchSpider, self).__init__(*args, **kwargs)
        self.start_requests

    def start_requests(self):
        keyword_list = [self.stringextra]
        for keyword in keyword_list:
            amazon_search_url = f'https://www.amazon.in/s?k={keyword}&page=1'
            yield scrapy.Request(url=amazon_search_url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': 1})

    def discover_product_urls(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword'] 

        ## Discover Product URLs
        search_products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in search_products:
            relative_url = product.css("h2>a::attr(href)").get()
            product_url = urljoin('https://www.amazon.in/', relative_url).split("?")[0]
            yield scrapy.Request(url=product_url, callback=self.parse_product_data, meta={'keyword': keyword, 'page': page})
            
        ## to what pages it want to go
        # if page == 1:
        #     available_pages = response.xpath(
        #         '//*[contains(@class, "s-pagination-item")][not(has-class("s-pagination-separator"))]/text()'
        #     ).getall()

            # last_page = available_pages[-1]
            # for page_num in range(2, write page no):
            #     amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page={page_num}'
            #     yield scrapy.Request(url=amazon_search_url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': page_num})


    def parse_product_data(self, response):
        AmaProd={}
        FlipProd=FlipItem()

        a_image_data = json.loads(re.findall(r"colorImages':.*'initial':\s*(\[.+?\])},\n", response.text)[0])
        a_variant_data = re.findall(r'dimensionValuesDisplayData"\s*:\s* ({.+?}),\n', response.text)
        a_feature_bullets = [bullet.strip() for bullet in response.css("#feature-bullets li ::text").getall()]
        price = response.css('.a-price span[aria-hidden="true"] ::text').get("")
        if not price:
            price = response.css('.a-price .a-offscreen ::text').get("")
        AmaProd["name"] = response.css("#productTitle::text").get("").strip()
        AmaProd["price"]= price
        AmaProd["stars"]= response.css("i[data-hook=average-star-rating] ::text").get("").strip()
        AmaProd["rating_count"] = response.css("div[data-hook=total-review-count] ::text").get("").strip()
        AmaProd["feature_bullets"]= a_feature_bullets
        AmaProd["image"]= a_image_data
        AmaProd["variant_data"]= a_variant_data
        AmaProd['unique_id'] =self.unique_id

        prod= Product(unique_id=self.unique_id, name = AmaProd["name"], image= AmaProd["image"], price= price, stars= AmaProd["stars"], feature_bullets=a_feature_bullets, rating_count=AmaProd["rating_count"],variant_data= a_variant_data)
        prod.save()
        return AmaProd
    
from scrapy.crawler import CrawlerProcess
from django.http import HttpResponse
def run_spider():
    process = CrawlerProcess()
    process.crawl(AmazonSearchSpider)
    process.start()
    return HttpResponse("Scrapy spider executed and JSON file generated.")