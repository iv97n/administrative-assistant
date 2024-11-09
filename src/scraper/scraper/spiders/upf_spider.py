import scrapy
import os
import re
from urllib.parse import urlparse

class UpfSpider(scrapy.Spider):
    name = 'upf_spider'
    start_urls = ['https://www.upf.edu/web/secretaria-grau/tramits']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
        },
        "DEPTH_LIMIT": 2,
        'ROBOTSTXT_OBEY': True
    }

    def parse(self, response):
        content_type = response.headers.get('Content-Type', b'').decode('utf-8')
        filename = f"output_{response.url.split('/')[-1]}.data"

        if 'text' in content_type or 'json' in content_type:
            content = response.text
        
            content = self.clean_html(content)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            for link in response.css('a::attr(href)').getall():
                if link and link.startswith('/') or link.startswith(response.url):
                    absolute_url = response.urljoin(link)
                    yield scrapy.Request(absolute_url, callback=self.parse)
        else:
            content = response.body 

            with open(filename, 'wb') as f:
                f.write(content)
        """    
        for link in response.css('a::attr(href)').getall():
            if link and link.startswith('/') or link.startswith(response.url):
                absolute_url = response.urljoin(link)
                yield scrapy.Request(absolute_url, callback=self.parse)
        """
    
    def clean_html(self, text):
        # 1. Remove <script> and <style> content
        text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)

        # 2. Remove HTML comments
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

        # 3. Extract relevant content from <h1>, <h2>, <h3>, <p>, <ul>, <ol>, <li>, <a>
        text = re.sub(r'<h1.*?>(.*?)</h1>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<h2.*?>(.*?)</h2>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<h3.*?>(.*?)</h3>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<p.*?>(.*?)</p>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<a.*?>(.*?)</a>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<ul.*?>(.*?)</ul>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<ol.*?>(.*?)</ol>', r'\1\n', text, flags=re.DOTALL)
        text = re.sub(r'<li.*?>(.*?)</li>', r'\1\n', text, flags=re.DOTALL)

        # 4. Clean up any remaining HTML tags
        text = re.sub(r'<.*?>', '', text)

        text = '\n'.join([line.strip() for line in text.splitlines()])

        return '\n'.join([line for line in text.splitlines() if line.strip() != ''])
    
