import scrapy
import os
from urllib.parse import urlparse

class UpfSpider(scrapy.Spider):
    name = 'upf_spider'
    start_urls = ['https://www.upf.edu/']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
            'ROBOTSTXT_OBEY': True,
        }
    }

    def parse(self, response):
         # Create a unique file name based on the URL or any other identifier
        filename = f"output_{response.url.split('/')[-1]}.data"

        with open(filename, 'wb') as f:
                f.write(response.body)
                
        # Follow all internal links on the page (excluding external links)
        for link in response.css('a::attr(href)').getall():
            # Make sure the link is a valid internal URL
            if link and link.startswith('/') or link.startswith(response.url):
                absolute_url = response.urljoin(link)
                yield scrapy.Request(absolute_url, callback=self.parse)