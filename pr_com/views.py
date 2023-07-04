from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from amazon.amazon.items import AmazonItem
import asyncio
from amazon.amazon.spiders.amazon_search import run_spider
from scrapy.crawler import CrawlerProcess
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from pr_com.models import Product
from django.shortcuts import redirect, render, HttpResponse
# from pr_com.utils import URLUtil

# connect scrapyd service
scrapyd = ScrapydAPI('http://127.0.0.1:8000/')


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)  # check if url format is valid
    except ValidationError:
        return False

    return True


# @csrf_exempt
# @require_http_methods(['POST', 'GET']) # only get and post
# def crawl(request):
#     # Post requests are for new crawling tasks
#     if request.method == 'POST':

#         url = request.POST.get('url', None) # take url comes from client. (From an input may be?)

#         if not url:
#             return JsonResponse({'error': 'Missing  args'})

#         if not is_valid_url(url):
#             return JsonResponse({'error': 'URL is invalid'})

#         domain = urlparse(url).netloc # parse the url and extract the domain
#         unique_id = str(uuid4()) # create a unique ID.

#         # This is the custom settings for scrapy spider.
#         # We can send anything we want to use it inside spiders and pipelines.
#         # I mean, anything
#         settings = {
#             'unique_id': unique_id, # unique ID for each record for DB
#             'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
#         }

#         # Here we schedule a new crawling task from scrapyd.
#         # Notice that settings is a special argument name.
#         # But we can pass other arguments, though.
#         # This returns a ID which belongs and will be belong to this task
#         # We are goint to use that to check task's status.
#         task = scrapyd.schedule('default', 'icrawler',
#             settings=settings, url=url, domain=domain)

#         return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started' })

#     # Get requests are for getting result of a specific crawling task
#     elif request.method == 'GET':
#         # We were passed these from past request above. Remember ?
#         # They were trying to survive in client side.
#         # Now they are here again, thankfully. <3
#         # We passed them back to here to check the status of crawling
#         # And if crawling is completed, we respond back with a crawled data.
#         task_id = request.GET.get('task_id', None)
#         unique_id = request.GET.get('unique_id', None)

#         if not task_id or not unique_id:
#             return JsonResponse({'error': 'Missing args'})

#         # Here we check status of crawling that just started a few seconds ago.
#         # If it is finished, we can query from database and get results
#         # If it is not finished we can return active status
#         # Possible results are -> pending, running, finished
#         status = scrapyd.job_status('default', task_id)
#         if status == 'finished':
#             try:
#                 # this is the unique_id that we created even before crawling started.
#                 item = Product.objects.get(unique_id=unique_id)
#                 return JsonResponse({'data': item.to_dict['data']})
#             except Exception as e:
#                 return JsonResponse({'error': str(e)})
#         else:
#             return JsonResponse({'status': status})

# @csrf_exempt
# @require_http_methods(['POST'])
# def crawl2(request, stringextra):
#         if request.method == 'POST':
#             stringextra = stringextra # take url comes from client. (From an input may be?)

#             # domain = urlparse(url).netloc # parse the url and extract the domain
#             unique_id = str(uuid4()) # create a unique ID.

#             # This is the custom settings for scrapy spider.
#             # We can send anything we want to use it inside spiders and pipelines.
#             # I mean, anything
#             settings = {
#                 'unique_id': unique_id, # unique ID for each record for DB
#                 'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
#             }

#             # Here we schedule a new crawling task from scrapyd.
#             # Notice that settings is a special argument name.
#             # But we can pass other arguments, though.
#             # This returns a ID which belongs and will be belong to this task
#             # We are goint to use that to check task's status.
#             task = scrapyd.schedule('default', 'amazon_search',
#                 settings=settings, stringextra=stringextra, unique_id=unique_id )

#             return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started' })

# def run_spider():
#     process = CrawlerProcess()
#     process.crawl(AmazonSearchSpider)
#     process.start()
    # return render(request, 'cart.html')


# Function to extract Product Title
def ama_get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price


def ama_get_price(soup):

    try:
        price = soup.find("span", class_='a-price-whole').text
        cleaned_string = ''.join(filter(str.isdigit, price))
        price = int(cleaned_string)

    except AttributeError:
        price = ""

    return price

# Function to extract Product Rating


def ama_get_rating(soup):

    try:
        rating = soup.find(
            "i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews


def ama_get_review_count(soup):
    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status


def ama_get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = ""

    return available


def flip_get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("div", class_='_4rR01T').text

        # Inner NavigableString Object
        title_value = title

        # Title as a string value
        title_string = title_value

        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()

    except AttributeError:
        title_string = ""

    return title_string


def flip_get_price(soup):

    try:
        price = soup.find("div", class_='_30jeq3').text
        cleaned_string = ''.join(filter(str.isdigit, price))
        price = int(cleaned_string)

    except AttributeError:
        price = ""

    return price
# Function to extract Product Rating


def flip_get_rating(soup):

    try:
        rating = soup.find("div", class_='_3LWZlK').text

    except AttributeError:

        # try:
        # 	rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        # except:
        rating = ""

    return rating


def ama_discover_product_urls(url, HEADERS):

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product divs
    ama_product_divs = soup.find_all(
        "a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    ama_product_urls = []
    total = 0
    for prod in ama_product_divs:
        ama_product_url = urljoin("https://www.amazon.in/", prod.get("href"))
        ama_product_urls.append(ama_product_url)
        if (total < 2):
            URL = "https://api.scrapingdog.com/scrape?api_key=64a2938f92f9092f20d503cf&url=" + \
                ama_product_url+"/&dynamic=false"
            webpage = requests.get(URL, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "lxml")
            product = Product(name=ama_get_title(soup), price=ama_get_price(soup), stars=ama_get_rating(soup), rating_count=ama_get_review_count(
                soup), availability=ama_get_availability(soup), product_url=ama_product_url, onlineStore="Amazon")
            product.save()
            print("Product Title =", ama_get_title(soup))
            print("Product Price =", ama_get_price(soup))
            print("Product Rating =", ama_get_rating(soup))
            print("Number of Product Reviews =", ama_get_review_count(soup))
            print("Availability =", ama_get_availability(soup))
            print()
            print()
            total += 1


def flip_discover_product_urls(url, HEADERS):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all product divs
#   ama_product_divs = soup.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    flip_product_divs = soup.find_all("div", class_="_2kHMtA")
#   ama_product_urls = []
    flip_product_urls = []
    total = 0
    for prod in flip_product_divs:

        if (total < 2):
            soup = prod

            product = Product(name=flip_get_title(soup), price=flip_get_price(soup), stars=flip_get_rating(soup), rating_count=soup.find("span", class_="_2_R_DZ").text,
                              availability="In Stock", product_url=urljoin("https://www.flipkart.com/", soup.find("a", class_="_1fQZEK").get("href")), onlineStore="Flipkart")
            product.save()

            print("Product Title =", flip_get_title(soup))

            print("Product Price =", flip_get_price(soup))
            print("Product Rating =", flip_get_rating(soup))
            print("Rating Count=", soup.find(
                "span", class_="_2_R_DZ").text)
            print("Product Url=", urljoin("https://www.flipkart.com/",
                                          soup.find("a", class_="_1fQZEK").get("href")))
            print("Image link=", soup.find(
                "img", class_="_396cs4").get("src"))
            print("Desc", soup.find("ul", class_="_1xgFaf").text.split("|"))
            print()
            print()
            total += 1


def crawl2(request, stringextra):
    # loop = asyncio.new_event_loop()
    # loop.run_in_executor(None, run_spider)

    # Close the event loop to clean up resources
    # loop.close()
    # obj= gostring(gs= stringextra)
    # obj.save()
    # run_spider()
    # ama= AmazonItem()
    # Headers for request
    Product.objects.all().delete()
    stringextra = stringextra.replace(" ", "_")
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    url = "https://api.scrapingdog.com/scrape?api_key=64a2938f92f9092f20d503cf&url=https://www.amazon.in/s?k=" + \
        stringextra+"&page=1/&dynamic=false"
    ama_discover_product_urls(url, HEADERS)
    url = "https://api.scrapingdog.com/scrape?api_key=64a2938f92f9092f20d503cf&url=https://www.flipkart.com/search?q="+stringextra+"&page=1&dynamic=false"
    flip_discover_product_urls(url, HEADERS)
    return redirect("/view_cart")
    # return HttpResponse("Hi")


# from django.http import HttpResponse
# from pr_com.utils import run_spider

#    def run_spider_view(request):
    #    run_spider()
    #    return HttpResponse("Scrapy spider executed and JSON file generated.")


# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from amazon.amazon.spiders.amazon_search import AmazonSearchSpider

# def crawl2(request, stringextra):
#     # Instantiate the spider
#     spider = AmazonSearchSpider()

#     # Configure Scrapy settings
#     settings = get_project_settings()

#     # Create a Scrapy crawler process
#     crawler = CrawlerProcess(settings)

#     # Start the crawler with the spider
#     crawler.crawl(AmazonSearchSpider)

#     # Start the crawler process
#     crawler.start()

#     # Return a response or perform further actions
#     return HttpResponse("Spider executed successfully.")
