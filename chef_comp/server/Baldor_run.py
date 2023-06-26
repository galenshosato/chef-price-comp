from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import sys

project_root = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(project_root)

from chef_comp.spiders.BaldorSpider import BaldorSpider
from chef_comp.spiders.WholeSpider import WholeSpider




def handle_data(item, spider):
    # do something with the scraped data
    return item

process = CrawlerProcess(get_project_settings())
process.crawl(WholeSpider)
process.start()








