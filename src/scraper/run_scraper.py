from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.spiders.upf_spider import UpfSpider
from scraper import settings  

def run():
    settings = get_project_settings()

    process = CrawlerProcess(settings)
    process.crawl(UpfSpider)
    process.start()

if __name__ == "__main__":
    run()
