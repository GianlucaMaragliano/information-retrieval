from typing import Any
import scrapy
from scrapy.http import Response

class experimentArchiveSpider(scrapy.Spider):
    name = "experiment_archive"

    start_urls = ["https://www.experimentarchive.com/"]

    def parse(self, response: Response):

        for experiment in response.xpath("//div[@class='polaroidcontainer']"):
            title = experiment.xpath(".//h2[@class='polaroidrubrik']/text()").get()
            type = experiment.xpath(".//div[@class='polaroidkategori']/text()").get()
            description = experiment.xpath(".//div[@class='polaroidingress']/text()").get()

            yield {
                "title": title,
                "type": type,
                "description": description,
            }