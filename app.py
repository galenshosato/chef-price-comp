import csv
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from BaldorSpider import BaldorSpider

filename = sys.argv[1]
with open(filename, 'r') as f:
    reader=csv.reader(f)
    titles = [row[0] for row in reader]


def run_baldor_spider(titles):
    process = CrawlerProcess(get_project_settings())
    process.crawl(BaldorSpider, titles=titles)
    process.start()


run_baldor_spider(titles)
