from typing import Any
import scrapy
from scrapy.http import Response


# eval "$(/home/gianluca/anaconda3/bin/conda shell.bash hook)"
# conda activate scrapy_env
# scrapy crawl science_experiments -o science_experiments.json

class ScienceBuddiesSpider(scrapy.Spider):

    name = 'science_buddies'

    start_urls = ["https://www.sciencebuddies.org/science-experiments?p=1"]
    # https://stevespangler.com/experiments/

    def parse(self, response: Response):


        # for experiment in response.xpath("//div[@class='search-result search-result-grid page-break-avoid']"):
        experiment = response.xpath("//div[@class='search-result search-result-grid page-break-avoid']")[0]
        
        titles_span = experiment.xpath("//span[@class='title-name']/text()").getall()
        titles_a = experiment.xpath("//div[@class='search-title']/a/text()").getall()

        for t in titles_span + titles_a:
            yield   {
                "title": t,
            }

        # next_page = response.xpath("//a[@class='pager only-screen']/@nth-child(last())/@href").get()

        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)