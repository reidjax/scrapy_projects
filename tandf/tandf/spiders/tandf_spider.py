import scrapy

from tandf.items import TandFItem

class TandFSpider(scrapy.Spider):
    name = "tandf"
    allowed_domains = ["athletic.net"]
    start_urls = [
        "http://www.athletic.net/TrackAndField/Athlete.aspx?AID=851626"
    ]

    def parse(self, response):
        item = TandFItem()
        # item['year_head'] = response.xpath('//tbody/tr[@class = "headSeason"]/td/b/font/text()').extract()
        # item['event_head'] = response.xpath('//tbody/tr[@class = "headEvent"]/td/b/text()').extract()
        # item['result'] = response.xpath('//tbody/tr[contains(@id,"rID")]/td[@valign = "top"][2]/text()').extract()
        item['combined'] = response.xpath('//tbody/tr[@class = "headSeason"]/td/b/font/text()|//tbody/tr[@class = "headEvent"]/td/b/text()|//tbody/tr[contains(@id,"rID")]/td[@valign = "top"][2]/text()')
        yield item