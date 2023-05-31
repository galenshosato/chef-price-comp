from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from chef_comp.spiders.BaldorSpider import BaldorSpider


data = []


def handle_data(item, spider):
    # do something with the scraped data
    data.append(item)

process = CrawlerProcess(get_project_settings())
process.crawl(BaldorSpider)
process.start()


print(data[0])






