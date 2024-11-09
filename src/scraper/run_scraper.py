from scrapy.crawler import CrawlerProcess
from src.scraper.scraper.spiders.upf_spider import UpfSpider
from src.scraper.scraper import settings  

def run():
    process = CrawlerProcess(settings)
    process.crawl(UpfSpider)
    process.start()

if __name__ == "__main__":
    run()
