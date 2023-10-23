from typing import Any
import scrapy
from scrapy.http import Response


# eval "$(/home/gianluca/anaconda3/bin/conda shell.bash hook)"
# conda activate scrapy_env
# scrapy crawl science_experiments -o science_experiments.json

class ScienceExperimentsSpider(scrapy.Spider):

    name = 'science_experiments'

    start_urls = ["https://www.sciencebuddies.org/science-experiments?p=1"]

    def parse(self, response: Response):


        # for experiment in response.xpath("//div[@class='search-result search-result-grid page-break-avoid']"):
        experiment = response.xpath("//div[@class='search-result search-result-grid page-break-avoid']")[0]
        yield {
            "titles": experiment.xpath("//span[@class='title-name']/text()").getall(),
            # "link": experiment.xpath(".//a/@href"),
            }