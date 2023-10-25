from typing import Any
import scrapy
from scrapy.http import Response

class steveSpanglerSpider(scrapy.Spider):
    name = "steve_spangler"

    start_urls = ["https://stevespangler.com/experiments/"]

    def parse(self, response: Response):

        base_url = "https://stevespangler.com"

        for experiment in response.xpath("//article[@class='post']"):

            title = experiment.xpath(".//div[@class='text']/h3/text()").get()
            description = experiment.xpath(".//div[@class='text']/p/text()").get()
            link = experiment.xpath(".//div[@class='text']/div/a[@class='wp-block-button__link']/@href").get()

            yield {
                "title": title,
                "description": description,
                "link": base_url+link,
            }

            next_page = response.xpath("//a[@class='nextpostslink']/@href").get()

            if next_page:
                yield response.follow(url=next_page, callback=self.parse)