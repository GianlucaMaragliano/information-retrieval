from typing import Any
import scrapy
from scrapy.http import Response

# scrapy crawl experiment_archive -o experiment_archive.jsonl

class experimentArchiveSpider(scrapy.Spider):
    name = "experiment_archive"

    start_urls = ["https://www.experimentarchive.com/"]

    def parse(self, response: Response):

        base_url = "https://www.experimentarchive.com"

        for experiment in response.xpath("//div[@class='polaroidcontainer']"):
            title = experiment.xpath(".//h2[@class='polaroidrubrik']/text()").get()
            subject = experiment.xpath(".//div[@class='polaroidkategori']/text()").get()
            description = experiment.xpath(".//div[@class='polaroidingress']/text()").get()
            link = experiment.xpath(".//div[@class='polaroidcontainer_inre']/a/@href").get()

            yield {
                "title": title,
                "subject": subject,
                "description": description,
                "link": base_url + link
            }