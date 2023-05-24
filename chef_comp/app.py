import csv
import sys
import pandas as pd
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from chef_comp.spiders.BaldorSpider import BaldorSpider

filename = sys.argv[1]
with open(filename, 'r') as f:
    reader=csv.reader(f)
    titles = [row[0] for row in reader]



process = CrawlerProcess(get_project_settings())

def handle_data(item, spider):
    # do something with the scraped data
    print(item)

process.crawl(BaldorSpider, titles=titles)
process.start()

with open('output.json') as f:
    data = json.load(f)






