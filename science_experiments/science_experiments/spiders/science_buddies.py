from typing import Any
import scrapy
import re
from scrapy.http import Response


# eval "$(/home/gianluca/anaconda3/bin/conda shell.bash hook)"
# conda activate scrapy_env
# scrapy crawl science_buddies -o science_experiments.json

class ScienceBuddiesSpider(scrapy.Spider):

    name = 'science_buddies'

    start_urls = ["https://www.sciencebuddies.org/science-experiments?p=1"]
    # https://stevespangler.com/experiments/

    def parse(self, response: Response):

        base_url = "https://www.sciencebuddies.org"

        experiment = response.xpath("//div[@class='search-result search-result-grid page-break-avoid']")
        links = experiment.xpath(".//div[@class='search-title']/a/@href").extract()
        for link in links:
            if link:
                yield scrapy.Request(url=base_url + link, callback=self.parse_experiment)

    def parse_experiment(self, response: Response):
        title = response.xpath('.//div[@class="main-title"]/div[@class="main-title-left"]/h1/span[@class="title-name"]/text()').get()
        if not title:
            title = response.xpath('.//div[@class="main-title"]/div[@class="main-title-left"]/h1/text()').get()

        subject = response.xpath('.//div[@class="page-break-avoid"]/div[@class="summary"]/div[@class="summary-left"]/div[@class="pi-summary-content"]/a/span[@class="title-name"]/text()').get()
        if not subject:
            subject = ""
        
        target_h2 = response.xpath(f"//h2[@id='introduction']")
        if target_h2:
            explanation = target_h2.xpath('following-sibling::*[following::h3]').extract()
            # TODO explanation is getting too much content, reduce it up to Term and Concept

        clean_explanation = ""
        if explanation:
            for content in explanation:
                clean_text = re.sub('<[^<]+?>', '', content)
                clean_text = clean_text.replace('\r', '').replace('\n', '')
                clean_explanation += clean_text


        # TODO parse description after <h1\2> abstract </h2> //*[@id="abstract"]

        yield {
            "title": title, 
            "subject": subject,
            "link": response.url,
            "explanation": clean_explanation, 
        }



        # next_page = response.xpath("//a[@class='pager only-screen']/@nth-child(last())/@href").get()

        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)