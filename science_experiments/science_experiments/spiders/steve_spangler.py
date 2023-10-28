import scrapy
from scrapy.http import Response

# scrapy crawl steve_spangler -o steve_spangler.json

class steveSpanglerSpider(scrapy.Spider):
    name = "steve_spangler"

    start_urls = ["https://stevespangler.com/experiments/"]

    def parse(self, response: Response):

        base_url = "https://stevespangler.com"

        for experiment in response.xpath("//article[@class='post']"):

            title = experiment.xpath(".//div[@class='text']/h3/text()").get()
            description = experiment.xpath(".//div[@class='text']/p/text()").get()
            link = experiment.xpath(".//div[@class='text']/div/a[@class='wp-block-button__link']/@href").get()

            if link:
                yield scrapy.Request(url=base_url + link, callback=self.parse_explanation, cb_kwargs=dict(title=title, description=description))

            next_page = response.xpath("//a[@class='nextpostslink']/@href").get()

            if next_page:
                yield response.follow(url=next_page, callback=self.parse)

    def parse_explanation(self, response: Response, title, description):
        
        explanation = response.xpath("//div[@class='text']/p/text()").get()

        yield {
            "title": title,
            "description": description,
            "link": response.url,
            "explanation": explanation,
        }